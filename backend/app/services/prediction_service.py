from sqlalchemy.orm import Session
from app.models.prediction import Prediction
from app.models.stock import Stock
from app.schemas.prediction import PredictionCreate, PredictionOut
from app.services.auth_service import get_current_user
from fastapi import HTTPException, status


def create_prediction(db: Session, payload: PredictionCreate, user_id: int) -> PredictionOut:
    stock = db.query(Stock).filter(Stock.symbol == payload.stock_symbol.upper()).first()
    if not stock:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Stock not found')
    prediction = Prediction(
        user_id=user_id,
        stock_id=stock.id,
        model_id=1,
        predicted_price=182.4,
        confidence_score=0.84,
        recommendation='Buy',
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return PredictionOut(symbol=stock.symbol, predicted_price=float(prediction.predicted_price), confidence_score=float(prediction.confidence_score), recommendation=prediction.recommendation or 'Hold', model_name=payload.model_name)
