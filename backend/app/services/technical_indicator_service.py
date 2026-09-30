from typing import List
from sqlalchemy.orm import Session
from app.models.technical_indicator import TechnicalIndicator
from app.models.stock import Stock
from app.schemas.technical_indicator import TechnicalIndicatorCreate


def list_indicators(db: Session, stock_symbol: str) -> List[TechnicalIndicator]:
    stock = db.query(Stock).filter(Stock.symbol == stock_symbol.upper()).first()
    if not stock:
        raise ValueError('Stock not found')
    return db.query(TechnicalIndicator).filter(TechnicalIndicator.stock_id == stock.id).all()


def create_indicator(db: Session, payload: TechnicalIndicatorCreate) -> TechnicalIndicator:
    stock = db.query(Stock).filter(Stock.symbol == payload.stock_symbol.upper()).first()
    if not stock:
        raise ValueError('Stock not found')
    item = TechnicalIndicator(stock_id=stock.id, indicator_name=payload.indicator_name, indicator_value=payload.indicator_value, indicator_date=payload.indicator_date)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
