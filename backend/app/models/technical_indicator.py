from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class TechnicalIndicator(Base):
    __tablename__ = 'technical_indicators'

    id = Column(Integer, primary_key=True, index=True)
    stock_id = Column(Integer, ForeignKey('stocks.id'), nullable=False)
    indicator_name = Column(String(64), nullable=False)
    indicator_value = Column(Numeric(12, 4), nullable=False)
    indicator_date = Column(Date, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    stock = relationship('Stock')
