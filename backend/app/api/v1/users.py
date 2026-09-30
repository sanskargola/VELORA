from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.v1.deps import get_current_active_user
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserProfileOut, UserProfileUpdate
from app.services.auth_service import get_password_hash, verify_password

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/me', response_model=UserProfileOut)
def get_profile(current_user: User = Depends(get_current_active_user)) -> UserProfileOut:
    return UserProfileOut(id=current_user.id, email=current_user.email, role=current_user.role, is_verified=current_user.is_verified)


@router.put('/me', response_model=UserProfileOut)
def update_profile(payload: UserProfileUpdate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)) -> UserProfileOut:
    if payload.email:
        current_user.email = payload.email
    db.commit()
    db.refresh(current_user)
    return UserProfileOut(id=current_user.id, email=current_user.email, role=current_user.role, is_verified=current_user.is_verified)


@router.delete('/me', status_code=status.HTTP_204_NO_CONTENT)
def delete_account(current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)) -> None:
    db.delete(current_user)
    db.commit()


@router.post('/me/change-password')
def change_password(current_password: str, new_password: str, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)) -> dict:
    if not verify_password(current_password, current_user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Current password is incorrect')
    current_user.password_hash = get_password_hash(new_password)
    db.commit()
    return {'message': 'Password updated successfully'}
