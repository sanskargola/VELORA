from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    stock_id = Column(Integer, ForeignKey('stocks.id'), nullable=False)
    transaction_type = Column(String(16), nullable=False)
    quantity = Column(Numeric(12, 4), nullable=False)
    price_per_unit = Column(Numeric(12, 4), nullable=False)
    total_amount = Column(Numeric(12, 4), nullable=False)
    transaction_date = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship('User')
    stock = relationship('Stock')
