from pydantic import BaseModel
from typing import Optional


class StockBase(BaseModel):
    symbol: str
    company_name: str
    sector: Optional[str] = None
    market_cap: Optional[int] = None
    currency: str = 'USD'


class StockCreate(StockBase):
    pass


class StockOut(StockBase):
    id: int

    class Config:
        from_attributes = True


class StockSearchResult(BaseModel):
    symbol: str
    company_name: str
    sector: Optional[str] = None


class HistoricalPoint(BaseModel):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
