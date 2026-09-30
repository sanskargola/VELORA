from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, Numeric, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class HistoricalPrice(Base):
    __tablename__ = 'historical_prices'
    __table_args__ = (UniqueConstraint('stock_id', 'price_date', name='uq_stock_price_date'),)

    id = Column(Integer, primary_key=True, index=True)
    stock_id = Column(Integer, ForeignKey('stocks.id'), nullable=False)
    price_date = Column(Date, nullable=False)
    open_price = Column(Numeric(12, 4), nullable=False)
    high_price = Column(Numeric(12, 4), nullable=False)
    low_price = Column(Numeric(12, 4), nullable=False)
    close_price = Column(Numeric(12, 4), nullable=False)
    volume = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    stock = relationship('Stock', back_populates='historical_prices')
