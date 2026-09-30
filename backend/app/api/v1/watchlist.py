import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.v1.deps import get_current_active_user
from app.db.database import get_db
from app.models.user import User
from app.schemas.watchlist import WatchlistCreate, WatchlistOut
from app.services.watchlist_service import create_watchlist_item, delete_watchlist_item, list_watchlist

router = APIRouter(prefix='/watchlist', tags=['watchlist'])
logger = logging.getLogger('stockvision')

@router.get('/', response_model=list[WatchlistOut])
def list_watchlist_items(current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)) -> list[WatchlistOut]:
    items = list_watchlist(db, current_user.id)
    return [WatchlistOut(id=item.id, stock_symbol=item.stock.symbol) for item in items]

@router.post('/', response_model=WatchlistOut, status_code=status.HTTP_201_CREATED)
def create_item(payload: WatchlistCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)) -> WatchlistOut:
    try:
        item = create_watchlist_item(db, current_user.id, payload)
        return WatchlistOut(id=item.id, stock_symbol=item.stock.symbol)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

@router.delete('/{item_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)) -> None:
    from app.models.watchlist import Watchlist

    item = db.query(Watchlist).filter(Watchlist.id == item_id, Watchlist.user_id == current_user.id).first()
    if not item:
        raise HTTPException(status_code=404, detail='Watchlist item not found')
    delete_watchlist_item(db, item)
