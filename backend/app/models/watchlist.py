from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class Watchlist(Base):
    __tablename__ = 'watchlist'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    stock_id = Column(Integer, ForeignKey('stocks.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship('User')
    stock = relationship('Stock')
