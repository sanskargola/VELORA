from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.stock import Stock
from app.schemas.stock import StockCreate, StockSearchResult


def search_stocks(db: Session, query: str) -> List[StockSearchResult]:
    rows = db.query(Stock).filter(Stock.symbol.ilike(f'%{query}%')).limit(10).all()
    return [StockSearchResult(symbol=row.symbol, company_name=row.company_name, sector=row.sector) for row in rows]


def get_stock_by_symbol(db: Session, symbol: str) -> Optional[Stock]:
    return db.query(Stock).filter(Stock.symbol == symbol.upper()).first()


def list_stocks(db: Session, skip: int = 0, limit: int = 100) -> List[Stock]:
    return db.query(Stock).offset(skip).limit(limit).all()


def create_stock(db: Session, payload: StockCreate) -> Stock:
    stock = Stock(symbol=payload.symbol.upper(), company_name=payload.company_name, sector=payload.sector, market_cap=payload.market_cap, currency=payload.currency)
    db.add(stock)
    db.commit()
    db.refresh(stock)
    return stock


def update_stock(db: Session, stock: Stock, payload: StockCreate) -> Stock:
    stock.symbol = payload.symbol.upper()
    stock.company_name = payload.company_name
    stock.sector = payload.sector
    stock.market_cap = payload.market_cap
    stock.currency = payload.currency
    db.commit()
    db.refresh(stock)
    return stock


def delete_stock(db: Session, stock: Stock) -> None:
    db.delete(stock)
    db.commit()
