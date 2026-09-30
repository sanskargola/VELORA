import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.v1.deps import get_current_active_user
from app.db.database import get_db
from app.models.user import User
from app.schemas.portfolio import PortfolioItemCreate, PortfolioItemOut
from app.services.portfolio_service import create_portfolio_item, delete_portfolio_item, list_portfolio, update_portfolio_item

router = APIRouter(prefix='/portfolio', tags=['portfolio'])
logger = logging.getLogger('stockvision')

@router.get('/', response_model=list[PortfolioItemOut])
def get_portfolio(current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)) -> list[PortfolioItemOut]:
    items = list_portfolio(db, current_user.id)
    return [PortfolioItemOut(id=item.id, stock_symbol=item.stock.symbol, quantity=float(item.quantity), average_buy_price=float(item.average_buy_price), current_price=float(item.current_price)) for item in items]

@router.post('/', response_model=PortfolioItemOut, status_code=status.HTTP_201_CREATED)
def create_item(payload: PortfolioItemCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)) -> PortfolioItemOut:
    try:
        item = create_portfolio_item(db, current_user.id, payload)
        return PortfolioItemOut(id=item.id, stock_symbol=item.stock.symbol, quantity=float(item.quantity), average_buy_price=float(item.average_buy_price), current_price=float(item.current_price))
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

@router.put('/{item_id}', response_model=PortfolioItemOut)
def update_item(item_id: int, payload: PortfolioItemCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)) -> PortfolioItemOut:
    from app.models.portfolio import Portfolio

    item = db.query(Portfolio).filter(Portfolio.id == item_id, Portfolio.user_id == current_user.id).first()
    if not item:
        raise HTTPException(status_code=404, detail='Portfolio item not found')
    item = update_portfolio_item(db, item, payload)
    return PortfolioItemOut(id=item.id, stock_symbol=item.stock.symbol, quantity=float(item.quantity), average_buy_price=float(item.average_buy_price), current_price=float(item.current_price))


@router.delete('/{item_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)) -> None:
    from app.models.portfolio import Portfolio

    item = db.query(Portfolio).filter(Portfolio.id == item_id, Portfolio.user_id == current_user.id).first()
    if not item:
        raise HTTPException(status_code=404, detail='Portfolio item not found')
    delete_portfolio_item(db, item)
