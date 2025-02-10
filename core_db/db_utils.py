from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from typing import List, Dict, Any, Optional

DATABASE_URL = "sqlite:///./sme_finance.db"  # Or get this from config

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create(db: Session, obj):
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update(db: Session, obj, data: Dict[str, Any]):
    for key, value in data.items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete(db: Session, obj):
    db.delete(obj)
    db.commit()

def query(
    db: Session,
    model,
    filters: Optional[List[Dict[str, Any]]] = None,
    sort_by: Optional[str] = None,
    limit: Optional[int] = 100,
    offset: Optional[int] = None,
    joins: Optional[List[str]] = None,
):
    query = db.query(model)

    if filters:
        for filter_item in filters:
            for key, value in filter_item.items():
                if isinstance(value, list):
                    query = query.filter(getattr(model, key).in_(value))
                else:
                    query = query.filter(getattr(model, key) == value)

    if joins:
        for join in joins:
            query = query.join(getattr(model, join))

    if sort_by:
        query = query.order_by(text(sort_by))

    if offset:
        query = query.offset(offset)

    if limit:
        query = query.limit(limit)

    return query.all()
