# financial_app/backend/budgeting/api.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core_db.db_utils import get_db
from . import models, schemas

app = APIRouter()

# --- Budget Categories ---

@app.post("/budget-categories/", response_model=schemas.BudgetCategory)
def create_budget_category(
    category: schemas.BudgetCategoryCreate, db: Session = Depends(get_db)
):
    """Creates a new budget category."""
    db_category = models.BudgetCategory(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@app.get("/budget-categories/", response_model=List[schemas.BudgetCategory])
def read_budget_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieves all budget categories."""
    categories = db.query(models.BudgetCategory).offset(skip).limit(limit).all()
    return categories

@app.get("/budget-categories/{category_id}", response_model=schemas.BudgetCategory)
def read_budget_category(category_id: int, db: Session = Depends(get_db)):
    """Retrieves a specific budget category by ID."""
    db_category = db.query(models.BudgetCategory).filter(models.BudgetCategory.id == category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Budget category not found")
    return db_category

@app.put("/budget-categories/{category_id}", response_model=schemas.BudgetCategory)
def update_budget_category(
    category_id: int, category: schemas.BudgetCategoryUpdate, db: Session = Depends(get_db)
):
    """Updates a specific budget category."""
    db_category = db.query(models.BudgetCategory).filter(models.BudgetCategory.id == category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Budget category not found")

    for key, value in category.dict(exclude_unset=True).items():
        setattr(db_category, key, value)

    db.commit()
    db.refresh(db_category)
    return db_category

@app.delete("/budget-categories/{category_id}")
def delete_budget_category(category_id: int, db: Session = Depends(get_db)):
    """Deletes a specific budget category."""
    db_category = db.query(models.BudgetCategory).filter(models.BudgetCategory.id == category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Budget category not found")
    db.delete(db_category)
    db.commit()
    return {"message": "Budget category deleted"}

# --- Budgets ---

@app.post("/budgets/", response_model=schemas.Budget)
def create_budget(budget: schemas.BudgetCreate, db: Session = Depends(get_db)):
    """Creates a new budget."""
    # Validate budget category IDs
    for entry in budget.entries:
        db_category = db.query(models.BudgetCategory).filter(models.BudgetCategory.id == entry.category_id).first()
        if db_category is None:
            raise HTTPException(status_code=400, detail=f"Budget category with ID {entry.category_id} not found")
    
    db_budget = models.Budget(
        name=budget.name,
        start_date=budget.start_date,
        end_date=budget.end_date
    )
    
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    
    # Create budget entries
    for entry in budget.entries:
        db_entry = models.BudgetEntry(
            budget_id=db_budget.id,
            category_id=entry.category_id,
            amount=entry.amount
        )
        db.add(db_entry)
    
    db.commit()
    return db_budget

@app.get("/budgets/", response_model=List[schemas.Budget])
def read_budgets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieves all budgets."""
    budgets = db.query(models.Budget).offset(skip).limit(limit).all()
    return budgets

@app.get("/budgets/{budget_id}", response_model=schemas.Budget)
def read_budget(budget_id: int, db: Session = Depends(get_db)):
    """Retrieves a specific budget by ID."""
    budget = db.query(models.Budget).filter(models.Budget.id == budget_id).first()
    if budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    return budget

@app.put("/budgets/{budget_id}", response_model=schemas.Budget)
def update_budget(budget_id: int, budget: schemas.BudgetUpdate, db: Session = Depends(get_db)):
    """Updates a specific budget."""
    db_budget = db.query(models.Budget).filter(models.Budget.id == budget_id).first()
    if db_budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    
    if budget.name:
        db_budget.name = budget.name
    if budget.start_date:
        db_budget.start_date = budget.start_date
    if budget.end_date:
        db_budget.end_date = budget.end_date

    # Update budget entries
    if budget.entries:
        for entry in budget.entries:
            db_entry = db.query(models.BudgetEntry).filter(
                models.BudgetEntry.budget_id == budget_id,
                models.BudgetEntry.category_id == entry.category_id
            ).first()
            if db_entry:
                db_entry.amount = entry.amount
            else:
                # Create a new entry if it doesn't exist
                db_entry = models.BudgetEntry(
                    budget_id=budget_id,
                    category_id=entry.category_id,
                    amount=entry.amount
                )
                db.add(db_entry)

    db.commit()
    db.refresh(db_budget)
    return db_budget

@app.delete("/budgets/{budget_id}")
def delete_budget(budget_id: int, db: Session = Depends(get_db)):
    """Deletes a specific budget."""
    db_budget = db.query(models.Budget).filter(models.Budget.id == budget_id).first()
    if db_budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    
    # Delete associated budget entries first
    db.query(models.BudgetEntry).filter(models.BudgetEntry.budget_id == budget_id).delete()
    
    db.delete(db_budget)
    db.commit()
    return {"message": "Budget deleted"}