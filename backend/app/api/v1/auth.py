from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.v1.deps import get_current_active_user
from app.db.database import get_db
from app.schemas.auth import LoginRequest, PasswordResetConfirm, PasswordResetRequest, TokenPair, UserCreate
from app.services.auth_service import create_refresh_token, get_current_user, login_user, register_user, update_password
from app.models.user import User

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/register', response_model=TokenPair, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)) -> TokenPair:
    register_user(db, payload)
    return login_user(db, LoginRequest(email=payload.email, password=payload.password))


@router.post('/login', response_model=TokenPair)
def login(payload: LoginRequest, db: Session = Depends(get_db)) -> TokenPair:
    return login_user(db, payload)


@router.post('/refresh', response_model=TokenPair)
def refresh_token(token: str, db: Session = Depends(get_db)) -> TokenPair:
    user = get_current_user(db, token)
    refresh = create_refresh_token(str(user.id))
    access = create_refresh_token(str(user.id))
    return TokenPair(access_token=access, refresh_token=refresh)


@router.post('/logout')
def logout(current_user: User = Depends(get_current_active_user)) -> dict:
    return {'message': 'Logged out successfully', 'user_id': current_user.id}


@router.post('/forgot-password')
def forgot_password(payload: PasswordResetRequest, db: Session = Depends(get_db)) -> dict:
    user = db.query(User).filter(User.email == str(payload.email)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return {'message': 'Password reset email sent'}


@router.post('/reset-password')
def reset_password(payload: PasswordResetConfirm, db: Session = Depends(get_db)) -> dict:
    updated = update_password(db, payload.token, payload.new_password)
    return {'message': 'Password reset successfully', 'user_id': updated.id}
