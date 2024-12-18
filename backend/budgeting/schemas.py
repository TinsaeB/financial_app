# financial_app/backend/budgeting/schemas.py
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import date

class BudgetCategoryBase(BaseModel):
    name: str = Field(..., example="Marketing")
    description: Optional[str] = Field(None, example="Expenses related to marketing campaigns")

class BudgetCategoryCreate(BudgetCategoryBase):
    pass

class BudgetCategoryUpdate(BudgetCategoryBase):
    name: Optional[str] = Field(None, example="Sales")
    description: Optional[str] = Field(None, example="Expenses related to sales activities")

class BudgetCategory(BudgetCategoryBase):
    id: int

    class Config:
        orm_mode = True

class BudgetEntryBase(BaseModel):
    category_id: int = Field(..., example=1)
    amount: float = Field(..., example=1000.00)

class BudgetEntryCreate(BudgetEntryBase):
    pass

class BudgetEntryUpdate(BaseModel):
    amount: float = Field(..., example=1200.50)

class BudgetEntry(BudgetEntryBase):
    id: int
    budget_id: int

    class Config:
        orm_mode = True

class BudgetBase(BaseModel):
    name: str = Field(..., example="Q1 2024 Budget")
    start_date: date = Field(..., example="2024-01-01")
    end_date: date = Field(..., example="2024-03-31")

class BudgetCreate(BudgetBase):
    entries: List[BudgetEntryCreate] = Field(..., example=[{"category_id": 1, "amount": 1000.00}])

class BudgetUpdate(BaseModel):
    name: Optional[str] = Field(None, example="Revised Q1 2024 Budget")
    start_date: Optional[date] = Field(None, example="2024-01-15")
    end_date: Optional[date] = Field(None, example="2024-04-15")
    entries: Optional[List[BudgetEntryUpdate]] = Field(None, example=[{"category_id": 1, "amount": 1200.50}])

class Budget(BudgetBase):
    id: int
    entries: List[BudgetEntry]

    class Config:
        orm_mode = True