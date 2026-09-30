import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.v1.deps import get_current_active_user
from app.db.database import get_db
from app.models.user import User
from app.schemas.news import NewsCreate, NewsOut
from app.services.news_service import create_news, delete_news, list_news, update_news
from app.models.news import News

router = APIRouter(prefix='/news', tags=['news'])
logger = logging.getLogger('stockvision')

@router.get('/', response_model=list[NewsOut])
def list_news_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[NewsOut]:
    items = list_news(db, skip=skip, limit=limit)
    return [NewsOut(id=item.id, title=item.title, content=item.content, source=item.source, url=item.url) for item in items]

@router.post('/', response_model=NewsOut, status_code=status.HTTP_201_CREATED)
def create_item(payload: NewsCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)) -> NewsOut:
    item = create_news(db, payload)
    return NewsOut(id=item.id, title=item.title, content=item.content, source=item.source, url=item.url)

@router.put('/{item_id}', response_model=NewsOut)
def update_item(item_id: int, payload: NewsCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)) -> NewsOut:
    item = db.query(News).filter(News.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail='News item not found')
    item = update_news(db, item, payload)
    return NewsOut(id=item.id, title=item.title, content=item.content, source=item.source, url=item.url)

@router.delete('/{item_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)) -> None:
    item = db.query(News).filter(News.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail='News item not found')
    delete_news(db, item)
