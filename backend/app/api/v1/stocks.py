import logging
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.stock import HistoricalPoint, StockCreate, StockOut, StockSearchResult
from app.services.stock_service import create_stock, delete_stock, get_stock_by_symbol, list_stocks, search_stocks, update_stock

router = APIRouter(prefix='/stocks', tags=['stocks'])
logger = logging.getLogger('stockvision')

@router.get('/', response_model=list[StockOut])
def list_stock_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[StockOut]:
    stocks = list_stocks(db, skip=skip, limit=limit)
    return [StockOut(id=stock.id, symbol=stock.symbol, company_name=stock.company_name, sector=stock.sector, market_cap=stock.market_cap, currency=stock.currency) for stock in stocks]

@router.post('/', response_model=StockOut, status_code=status.HTTP_201_CREATED)
def create_stock_item(payload: StockCreate, db: Session = Depends(get_db)) -> StockOut:
    try:
        stock = create_stock(db, payload)
        return StockOut(id=stock.id, symbol=stock.symbol, company_name=stock.company_name, sector=stock.sector, market_cap=stock.market_cap, currency=stock.currency)
    except Exception as exc:
        logger.exception('Failed to create stock')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

@router.get('/search', response_model=list[StockSearchResult])
def search(query: str = Query(..., min_length=1), db: Session = Depends(get_db)) -> list[StockSearchResult]:
    return search_stocks(db, query)

@router.get('/{symbol}', response_model=StockOut)
def get_stock(symbol: str, db: Session = Depends(get_db)) -> StockOut:
    stock = get_stock_by_symbol(db, symbol)
    if not stock:
        raise HTTPException(status_code=404, detail='Stock not found')
    return StockOut(id=stock.id, symbol=stock.symbol, company_name=stock.company_name, sector=stock.sector, market_cap=stock.market_cap, currency=stock.currency)

@router.put('/{symbol}', response_model=StockOut)
def update_stock_item(symbol: str, payload: StockCreate, db: Session = Depends(get_db)) -> StockOut:
    stock = get_stock_by_symbol(db, symbol)
    if not stock:
        raise HTTPException(status_code=404, detail='Stock not found')
    stock = update_stock(db, stock, payload)
    return StockOut(id=stock.id, symbol=stock.symbol, company_name=stock.company_name, sector=stock.sector, market_cap=stock.market_cap, currency=stock.currency)

@router.delete('/{symbol}', status_code=status.HTTP_204_NO_CONTENT)
def delete_stock_item(symbol: str, db: Session = Depends(get_db)) -> None:
    stock = get_stock_by_symbol(db, symbol)
    if not stock:
        raise HTTPException(status_code=404, detail='Stock not found')
    delete_stock(db, stock)

@router.get('/{symbol}/history', response_model=list[HistoricalPoint])
def history(symbol: str, db: Session = Depends(get_db)) -> list[HistoricalPoint]:
    return [HistoricalPoint(date='2024-01-01', open=100.0, high=105.0, low=98.0, close=103.0, volume=1000000)]
