from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.v1.deps import get_current_active_user
from app.db.database import get_db
from app.models.portfolio import Portfolio
from app.models.prediction import Prediction
from app.models.stock import Stock
from app.models.user import User
from app.models.watchlist import Watchlist
from app.schemas.admin import AdminStatsOut, AdminUserOut, ModelPerformanceOut, PredictionLogOut

router = APIRouter(prefix='/admin', tags=['admin'])


def require_admin(current_user: User = Depends(get_current_active_user)) -> User:
    if current_user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Admin access required')
    return current_user


@router.get('/health')
def admin_health(current_user: User = Depends(require_admin)) -> dict:
    return {'message': 'Admin endpoint', 'user_id': current_user.id, 'role': current_user.role}


@router.get('/users', response_model=list[AdminUserOut])
def list_users(db: Session = Depends(get_db), current_user: User = Depends(require_admin)) -> list[AdminUserOut]:
    users = db.query(User).all()
    return [AdminUserOut(id=user.id, email=user.email, role=user.role, is_verified=user.is_verified) for user in users]


@router.get('/stats', response_model=AdminStatsOut)
def stats(db: Session = Depends(get_db), current_user: User = Depends(require_admin)) -> AdminStatsOut:
    return AdminStatsOut(
        users=db.query(User).count(),
        stocks=db.query(Stock).count(),
        predictions=db.query(Prediction).count(),
        watchlist_items=db.query(Watchlist).count(),
        portfolio_items=db.query(Portfolio).count(),
    )


@router.get('/predictions', response_model=list[PredictionLogOut])
def prediction_logs(db: Session = Depends(get_db), current_user: User = Depends(require_admin)) -> list[PredictionLogOut]:
    preds = db.query(Prediction).all()
    return [PredictionLogOut(id=p.id, symbol=p.stock.symbol, model_name=p.model_name, recommendation=p.recommendation, confidence_score=float(p.confidence_score)) for p in preds]


@router.get('/models', response_model=list[ModelPerformanceOut])
def model_performance(db: Session = Depends(get_db), current_user: User = Depends(require_admin)) -> list[ModelPerformanceOut]:
    rows = db.query(Prediction.model_name, Prediction.confidence_score).all()
    grouped: dict[str, list[float]] = {}
    for name, score in rows:
        grouped.setdefault(name, []).append(float(score))
    return [ModelPerformanceOut(model_name=name, average_confidence=sum(scores) / len(scores), total_predictions=len(scores)) for name, scores in grouped.items()]
