from pydantic import BaseModel
from typing import Optional


class PredictionCreate(BaseModel):
    stock_symbol: str
    model_name: str
    timeframe: str = '7d'


class PredictionOut(BaseModel):
    symbol: str
    predicted_price: float
    confidence_score: float
    recommendation: str
    model_name: str

    class Config:
        from_attributes = True
