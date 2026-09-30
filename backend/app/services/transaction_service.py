from typing import List
from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.models.stock import Stock
from app.schemas.transaction import TransactionCreate


def list_transactions(db: Session, user_id: int) -> List[Transaction]:
    return db.query(Transaction).filter(Transaction.user_id == user_id).all()


def create_transaction(db: Session, user_id: int, payload: TransactionCreate) -> Transaction:
    stock = db.query(Stock).filter(Stock.symbol == payload.stock_symbol.upper()).first()
    if not stock:
        raise ValueError('Stock not found')
    total_amount = payload.quantity * payload.price_per_unit
    item = Transaction(user_id=user_id, stock_id=stock.id, transaction_type=payload.transaction_type, quantity=payload.quantity, price_per_unit=payload.price_per_unit, total_amount=total_amount)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
