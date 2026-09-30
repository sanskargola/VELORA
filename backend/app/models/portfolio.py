from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class Portfolio(Base):
    __tablename__ = 'portfolio'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    stock_id = Column(Integer, ForeignKey('stocks.id'), nullable=False)
    quantity = Column(Numeric(12, 4), nullable=False, default=0)
    average_buy_price = Column(Numeric(12, 4), nullable=False)
    current_price = Column(Numeric(12, 4), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship('User')
    stock = relationship('Stock')
