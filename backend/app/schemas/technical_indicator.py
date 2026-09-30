from pydantic import BaseModel
from datetime import date


class TechnicalIndicatorCreate(BaseModel):
    stock_symbol: str
    indicator_name: str
    indicator_value: float
    indicator_date: date


class TechnicalIndicatorOut(BaseModel):
    id: int
    stock_symbol: str
    indicator_name: str
    indicator_value: float
    indicator_date: date

    class Config:
        from_attributes = True
