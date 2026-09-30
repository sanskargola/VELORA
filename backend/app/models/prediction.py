from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    stock_id = Column(Integer, ForeignKey('stocks.id'), nullable=False)
    model_name = Column(String(64), nullable=False)
    predicted_price = Column(Numeric(12, 4), nullable=False)
    confidence_score = Column(Numeric(6, 4), nullable=False)
    recommendation = Column(String(16), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship('User')
    stock = relationship('Stock')
    history = relationship('PredictionHistory', back_populates='prediction', cascade='all, delete-orphan')


class PredictionHistory(Base):
    __tablename__ = 'prediction_history'

    id = Column(Integer, primary_key=True, index=True)
    prediction_id = Column(Integer, ForeignKey('predictions.id'), nullable=False)
    recorded_at = Column(DateTime(timezone=True), server_default=func.now())
    predicted_price = Column(Numeric(12, 4), nullable=False)
    confidence_score = Column(Numeric(6, 4), nullable=False)
    recommendation = Column(String(16), nullable=False)

    prediction = relationship('Prediction', back_populates='history')
