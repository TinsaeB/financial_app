from fastapi import FastAPI, Depends, HTTPException
from . import models, schemas
from core_db.db_utils import get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/accounts/", response_model=schemas.Account)
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    db_account = models.Account(**account.dict())
    return db.create(db_account)

@app.get("/accounts/", response_model=list[schemas.Account])
def get_accounts(db: Session = Depends(get_db)):
    return db.query(models.Account).all()

@app.get("/accounts/{account_id}", response_model=schemas.Account)
def get_account(account_id: int, db: Session = Depends(get_db)):
    db_account = db.query(models.Account).filter(models.Account.id == account_id).first()
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@app.post("/transactions/", response_model=schemas.Transaction)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = models.Transaction(**transaction.dict())
    return db.create(db_transaction)

@app.get("/transactions/", response_model=list[schemas.Transaction])
def get_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).all()

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
