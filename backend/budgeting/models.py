# financial_app/backend/budgeting/models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from core_db.db_utils import Base  # Assuming you're using SQLAlchemy declarative base

class BudgetCategory(Base):
    __tablename__ = "budget_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)

    budgets = relationship("Budget", secondary="budget_entries", back_populates="categories")

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

    entries = relationship("BudgetEntry", back_populates="budget")
    categories = relationship("BudgetCategory", secondary="budget_entries", back_populates="budgets")

class BudgetEntry(Base):
    __tablename__ = "budget_entries"
    id = Column(Integer, primary_key=True, index=True)
    budget_id = Column(Integer, ForeignKey("budgets.id"))
    category_id = Column(Integer, ForeignKey("budget_categories.id"))
    amount = Column(Float)

    budget = relationship("Budget", back_populates="entries")
    category = relationship("BudgetCategory")