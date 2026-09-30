from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.portfolio import Portfolio
from app.models.stock import Stock
from app.schemas.portfolio import PortfolioItemCreate


def list_portfolio(db: Session, user_id: int) -> List[Portfolio]:
    return db.query(Portfolio).filter(Portfolio.user_id == user_id).all()


def create_portfolio_item(db: Session, user_id: int, payload: PortfolioItemCreate) -> Portfolio:
    stock = db.query(Stock).filter(Stock.symbol == payload.stock_symbol.upper()).first()
    if not stock:
        raise ValueError('Stock not found')
    item = Portfolio(user_id=user_id, stock_id=stock.id, quantity=payload.quantity, average_buy_price=payload.average_buy_price, current_price=payload.current_price)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_portfolio_item(db: Session, item: Portfolio, payload: PortfolioItemCreate) -> Portfolio:
    item.quantity = payload.quantity
    item.average_buy_price = payload.average_buy_price
    item.current_price = payload.current_price
    db.commit()
    db.refresh(item)
    return item


def delete_portfolio_item(db: Session, item: Portfolio) -> None:
    db.delete(item)
    db.commit()
