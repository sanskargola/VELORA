from typing import List
from sqlalchemy.orm import Session
from app.models.news import News
from app.schemas.news import NewsCreate


def list_news(db: Session, skip: int = 0, limit: int = 100) -> List[News]:
    return db.query(News).offset(skip).limit(limit).all()


def create_news(db: Session, payload: NewsCreate) -> News:
    item = News(title=payload.title, content=payload.content, source=payload.source, url=payload.url)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_news(db: Session, item: News, payload: NewsCreate) -> News:
    item.title = payload.title
    item.content = payload.content
    item.source = payload.source
    item.url = payload.url
    db.commit()
    db.refresh(item)
    return item


def delete_news(db: Session, item: News) -> None:
    db.delete(item)
    db.commit()
