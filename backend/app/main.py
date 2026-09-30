import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import OperationalError

from app.api.v1 import admin, auth, news, portfolio, predictions, stocks, users, watchlist
from app.db.database import Base, engine

logger = logging.getLogger('stockvision')

try:
    Base.metadata.create_all(bind=engine)
except OperationalError as exc:
    logger.warning('Database initialization skipped: %s', exc)

app = FastAPI(title='StockVision AI API', version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth.router, prefix='/api/v1')
app.include_router(users.router, prefix='/api/v1')
app.include_router(stocks.router, prefix='/api/v1')
app.include_router(predictions.router, prefix='/api/v1')
app.include_router(portfolio.router, prefix='/api/v1')
app.include_router(watchlist.router, prefix='/api/v1')
app.include_router(news.router, prefix='/api/v1')
app.include_router(admin.router, prefix='/api/v1')

@app.get('/health')
def health() -> dict:
    return {'status': 'ok'}
