from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.v1.deps import get_current_active_user
from app.db.database import get_db
from app.models.prediction import Prediction
from app.models.user import User
from app.schemas.prediction import PredictionCreate, PredictionOut
from app.services.prediction_service import create_prediction

router = APIRouter(prefix='/predictions', tags=['predictions'])


@router.post('/', response_model=PredictionOut, status_code=status.HTTP_201_CREATED)
def predict(payload: PredictionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)) -> PredictionOut:
    return create_prediction(db, payload, current_user.id)


@router.get('/history', response_model=list[PredictionOut])
def prediction_history(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)) -> list[PredictionOut]:
    predictions = db.query(Prediction).filter(Prediction.user_id == current_user.id).all()
    return [PredictionOut(symbol=p.stock.symbol, predicted_price=float(p.predicted_price), confidence_score=float(p.confidence_score), recommendation=p.recommendation, model_name=p.model_name) for p in predictions]


@router.get('/{prediction_id}', response_model=PredictionOut)
def get_prediction(prediction_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)) -> PredictionOut:
    prediction = db.query(Prediction).filter(Prediction.id == prediction_id, Prediction.user_id == current_user.id).first()
    if not prediction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Prediction not found')
    return PredictionOut(symbol=prediction.stock.symbol, predicted_price=float(prediction.predicted_price), confidence_score=float(prediction.confidence_score), recommendation=prediction.recommendation, model_name=prediction.model_name)
