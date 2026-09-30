from sqlalchemy import Column, Integer, String, BigInteger, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(16), unique=True, nullable=False, index=True)
    company_name = Column(String(255), nullable=False)
    sector = Column(String(128))
    market_cap = Column(BigInteger)
    currency = Column(String(8), default='USD')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    historical_prices = relationship('HistoricalPrice', back_populates='stock', cascade='all, delete-orphan')
    predictions = relationship('Prediction', back_populates='stock')
    portfolio_items = relationship('Portfolio', back_populates='stock')
    watchlist_items = relationship('Watchlist', back_populates='stock')
    transactions = relationship('Transaction', back_populates='stock')
    technical_indicators = relationship('TechnicalIndicator', back_populates='stock')
