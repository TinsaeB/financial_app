from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
# Assuming you have a way to access Django models across services, or you can redefine them here
from purchasing.models import Supplier 

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

# Example usage for querying a supplier
def get_supplier(db: Session, supplier_id: int):
    return db.query(Supplier).filter(Supplier.id == supplier_id).first()

# ... other CRUD and utility functions
