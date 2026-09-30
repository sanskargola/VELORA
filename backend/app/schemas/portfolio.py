from typing import Optional
from pydantic import BaseModel


class PortfolioItemCreate(BaseModel):
    stock_symbol: str
    quantity: float
    average_buy_price: float
    current_price: float


class PortfolioItemOut(BaseModel):
    id: int
    stock_symbol: str
    quantity: float
    average_buy_price: float
    current_price: float

    class Config:
        from_attributes = True
