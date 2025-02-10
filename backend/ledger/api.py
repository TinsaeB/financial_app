from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core_db.db_utils import get_db, create, query
from . import models, schemas
from sqlalchemy import func

app = APIRouter()

# --- Accounts ---

@app.post("/accounts/", response_model=schemas.Account)
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    db_account = models.Account(**account.dict())
    return create(db, db_account)

@app.get("/accounts/", response_model=List[schemas.Account])
def get_accounts(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return query(db, models.Account, offset=skip, limit=limit)

@app.get("/accounts/{account_id}", response_model=schemas.Account)
def get_account(account_id: int, db: Session = Depends(get_db)):
    db_account = db.query(models.Account).filter(models.Account.id == account_id).first()
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

# --- Transactions ---

@app.post("/transactions/", response_model=schemas.Transaction)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = models.Transaction(**transaction.dict())
    return create(db, db_transaction)

@app.get("/transactions/", response_model=List[schemas.Transaction])
def get_transactions(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return query(db, models.Transaction, offset=skip, limit=limit)

# --- Journal Entries ---

@app.post("/journal-entries/", response_model=schemas.JournalEntry)
def create_journal_entry(entry: schemas.JournalEntryCreate, db: Session = Depends(get_db)):
    db_entry = models.JournalEntry(**entry.dict())
    return create(db, db_entry)

@app.get("/journal-entries/", response_model=List[schemas.JournalEntry])
def get_journal_entries(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return query(db, models.JournalEntry, offset=skip, limit=limit)

@app.put("/journal-entries/{entry_id}", response_model=schemas.JournalEntry)
def update_journal_entry(entry_id: int, entry: schemas.JournalEntryCreate, db: Session = Depends(get_db)):
    db_entry = db.query(models.JournalEntry).filter(models.JournalEntry.id == entry_id).first()
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    for key, value in entry.dict().items():
        setattr(db_entry, key, value)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@app.delete("/journal-entries/{entry_id}")
def delete_journal_entry(entry_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(models.JournalEntry).filter(models.JournalEntry.id == entry_id).first()
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    db.delete(db_entry)
    db.commit()
    return {"message": "Journal entry deleted"}

# --- Financial Statements ---

@app.get("/accounts/{account_id}/balance", response_model=float)
def get_account_balance(account_id: int, db: Session = Depends(get_db)):
    account = db.query(models.Account).filter(models.Account.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    debit_entries = db.query(models.JournalEntry).filter(models.JournalEntry.account_id == account_id, models.JournalEntry.entry_type == "Debit").all()
    credit_entries = db.query(models.JournalEntry).filter(models.JournalEntry.account_id == account_id, models.JournalEntry.entry_type == "Credit").all()
    
    debit_total = sum([entry.amount for entry in debit_entries])
    credit_total = sum([entry.amount for entry in credit_entries])
    
    if account.account_type in ["Asset", "Expense"]:
        return debit_total - credit_total
    elif account.account_type in ["Liability", "Equity", "Revenue"]:
        return credit_total - debit_total
    else:
        raise HTTPException(status_code=400, detail="Invalid account type")

@app.get("/trial-balance", response_model=dict)
def get_trial_balance(db: Session = Depends(get_db)):
    accounts = db.query(models.Account).all()
    trial_balance = {}
    for account in accounts:
        balance = get_account_balance(account.id, db)
        trial_balance[account.name] = balance
    return trial_balance

@app.get("/income-statement", response_model=dict)
def get_income_statement(db: Session = Depends(get_db)):
    revenue_accounts = db.query(models.Account).filter(models.Account.account_type == "Revenue").all()
    expense_accounts = db.query(models.Account).filter(models.Account.account_type == "Expense").all()

    revenue_total = sum([get_account_balance(account.id, db) for account in revenue_accounts])
    expense_total = sum([get_account_balance(account.id, db) for account in expense_accounts])
    
    cogs_total = sum([get_account_balance(account.id, db) for account in expense_accounts if account.name == "Cost of Goods Sold"])
    
    gross_profit = revenue_total - cogs_total
    net_income = revenue_total - expense_total

    return {
        "revenue": revenue_total,
        "expenses": expense_total,
        "cogs": cogs_total,
        "gross_profit": gross_profit,
        "net_income": net_income,
    }

@app.get("/balance-sheet", response_model=dict)
def get_balance_sheet(db: Session = Depends(get_db)):
    asset_accounts = db.query(models.Account).filter(models.Account.account_type == "Asset").all()
    liability_accounts = db.query(models.Account).filter(models.Account.account_type == "Liability").all()
    equity_accounts = db.query(models.Account).filter(models.Account.account_type == "Equity").all()

    total_assets = sum([get_account_balance(account.id, db) for account in asset_accounts])
    total_liabilities = sum([get_account_balance(account.id, db) for account in liability_accounts])
    total_equity = sum([get_account_balance(account.id, db) for account in equity_accounts])

    return {
        "assets": total_assets,
        "liabilities": total_liabilities,
        "equity": total_equity,
    }

@app.get("/cash-flow-statement", response_model=dict)
def get_cash_flow_statement(db: Session = Depends(get_db)):
    # This is a simplified placeholder. A full implementation would require tracking cash flows from operating, investing, and financing activities.
    net_income = get_income_statement(db)["net_income"]
    
    # Placeholder for adjustments and other cash flow items
    adjustments = 0
    cash_from_operating_activities = net_income + adjustments
    
    return {
        "cash_from_operating_activities": cash_from_operating_activities,
    }

@app.get("/aged-receivables", response_model=List[dict])
def get_aged_receivables(db: Session = Depends(get_db)):
    # Placeholder for a more complex implementation that would involve customer data and aging buckets
    receivables = db.query(models.JournalEntry).filter(models.JournalEntry.entry_type == "Debit").filter(models.JournalEntry.account.has(account_type="Asset")).all()
    
    aged_receivables = []
    for entry in receivables:
        aged_receivables.append({
            "account": entry.account.name,
            "amount": entry.amount,
            "days_outstanding": 0  # Placeholder
        })
    
    return aged_receivables

@app.get("/aged-payables", response_model=List[dict])
def get_aged_payables(db: Session = Depends(get_db)):
    # Placeholder for a more complex implementation that would involve supplier data and aging buckets
    payables = db.query(models.JournalEntry).filter(models.JournalEntry.entry_type == "Credit").filter(models.JournalEntry.account.has(account_type="Liability")).all()
    
    aged_payables = []
    for entry in payables:
        aged_payables.append({
            "account": entry.account.name,
            "amount": entry.amount,
            "days_outstanding": 0  # Placeholder
        })
    
    return aged_payables

@app.get("/general-ledger-detail", response_model=List[dict])
def get_general_ledger_detail(db: Session = Depends(get_db)):
    entries = db.query(models.JournalEntry).all()
    
    ledger_detail = []
    for entry in entries:
        ledger_detail.append({
            "date": entry.transaction.date,
            "account": entry.account.name,
            "description": entry.transaction.description,
            "debit" if entry.entry_type == "Debit" else "credit": entry.amount,
        })
    
    return ledger_detail
