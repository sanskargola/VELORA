from typing import List
from sqlalchemy.orm import Session
from app.models.watchlist import Watchlist
from app.models.stock import Stock
from app.schemas.watchlist import WatchlistCreate


def list_watchlist(db: Session, user_id: int) -> List[Watchlist]:
    return db.query(Watchlist).filter(Watchlist.user_id == user_id).all()


def create_watchlist_item(db: Session, user_id: int, payload: WatchlistCreate) -> Watchlist:
    stock = db.query(Stock).filter(Stock.symbol == payload.stock_symbol.upper()).first()
    if not stock:
        raise ValueError('Stock not found')
    item = Watchlist(user_id=user_id, stock_id=stock.id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def delete_watchlist_item(db: Session, item: Watchlist) -> None:
    db.delete(item)
    db.commit()
