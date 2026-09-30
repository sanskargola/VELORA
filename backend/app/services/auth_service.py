from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.core.config import settings
from app.models.user import User
from app.schemas.auth import LoginRequest, TokenPair, UserCreate

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    if expires_delta is None:
        expires_delta = timedelta(minutes=settings.access_token_expire_minutes)
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {'sub': subject, 'exp': expire}
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)


def create_refresh_token(subject: str) -> str:
    expires_delta = timedelta(minutes=settings.refresh_token_expire_minutes)
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {'sub': subject, 'exp': expire, 'type': 'refresh'}
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user


def register_user(db: Session, payload: UserCreate) -> User:
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email already registered')
    user = User(email=str(payload.email), password_hash=get_password_hash(payload.password), role='user')
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def login_user(db: Session, payload: LoginRequest) -> TokenPair:
    user = authenticate_user(db, str(payload.email), payload.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    access_token = create_access_token(str(user.id))
    refresh_token = create_refresh_token(str(user.id))
    return TokenPair(access_token=access_token, refresh_token=refresh_token)


def get_current_user(db: Session, token: str) -> User:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        user_id = payload.get('sub')
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
    except JWTError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token') from exc

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')
    return user


def create_refresh_token(subject: str) -> str:
    expires_delta = timedelta(minutes=settings.refresh_token_expire_minutes)
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {'sub': subject, 'exp': expire, 'type': 'refresh'}
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)


def update_password(db: Session, token: str, new_password: str) -> User:
    user = get_current_user(db, token)
    user.password_hash = get_password_hash(new_password)
    db.commit()
    db.refresh(user)
    return user
