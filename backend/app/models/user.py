from sqlalchemy import Boolean, Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum('admin', 'user', name='user_role'), default='user')
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    predictions = relationship('Prediction', back_populates='user')
    portfolio_items = relationship('Portfolio', back_populates='user')
    watchlist_items = relationship('Watchlist', back_populates='user')
    transactions = relationship('Transaction', back_populates='user')
