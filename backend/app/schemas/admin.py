from typing import List
from pydantic import BaseModel, ConfigDict


class AdminUserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    role: str
    is_verified: bool


class PredictionLogOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    symbol: str
    model_name: str
    recommendation: str
    confidence_score: float


class ModelPerformanceOut(BaseModel):
    model_name: str
    average_confidence: float
    total_predictions: int


class AdminStatsOut(BaseModel):
    users: int
    stocks: int
    predictions: int
    watchlist_items: int
    portfolio_items: int
