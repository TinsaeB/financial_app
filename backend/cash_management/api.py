from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core_db.db_utils import get_db, create
from . import models, schemas

app = APIRouter()

# --- Bank Accounts ---

@app.post("/bank-accounts/", response_model=schemas.BankAccount)
def create_bank_account(bank_account: schemas.BankAccountCreate, db: Session = Depends(get_db)):
    db_bank_account = models.BankAccount(**bank_account.dict())
    return create(db, db_bank_account)

@app.get("/bank-accounts/", response_model=List[schemas.BankAccount])
def get_bank_accounts(db: Session = Depends(get_db)):
    return db.query(models.BankAccount).all()

@app.get("/bank-accounts/{account_id}", response_model=schemas.BankAccount)
def get_bank_account(account_id: int, db: Session = Depends(get_db)):
    db_bank_account = db.query(models.BankAccount).filter(models.BankAccount.id == account_id).first()
    if not db_bank_account:
        raise HTTPException(status_code=404, detail="Bank account not found")
    return db_bank_account

@app.put("/bank-accounts/{account_id}", response_model=schemas.BankAccount)
def update_bank_account(account_id: int, bank_account: schemas.BankAccountUpdate, db: Session = Depends(get_db)):
    db_bank_account = db.query(models.BankAccount).filter(models.BankAccount.id == account_id).first()
    if not db_bank_account:
        raise HTTPException(status_code=404, detail="Bank account not found")
    for key, value in bank_account.dict(exclude_unset=True).items():
        setattr(db_bank_account, key, value)
    db.commit()
    db.refresh(db_bank_account)
    return db_bank_account

@app.delete("/bank-accounts/{account_id}")
def delete_bank_account(account_id: int, db: Session = Depends(get_db)):
    db_bank_account = db.query(models.BankAccount).filter(models.BankAccount.id == account_id).first()
    if not db_bank_account:
        raise HTTPException(status_code=404, detail="Bank account not found")
    db.delete(db_bank_account)
    db.commit()
    return {"message": "Bank account deleted successfully"}

# --- Cash Transactions ---

@app.post("/cash-transactions/", response_model=schemas.CashTransaction)
def create_cash_transaction(transaction: schemas.CashTransactionCreate, db: Session = Depends(get_db)):
    db_transaction = models.CashTransaction(**transaction.dict())
    return create(db, db_transaction)

@app.get("/cash-transactions/", response_model=List[schemas.CashTransaction])
def get_cash_transactions(db: Session = Depends(get_db)):
    return db.query(models.CashTransaction).all()

@app.get("/cash-transactions/{transaction_id}", response_model=schemas.CashTransaction)
def get_cash_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = db.query(models.CashTransaction).filter(models.CashTransaction.id == transaction_id).first()
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Cash transaction not found")
    return db_transaction

@app.put("/cash-transactions/{transaction_id}", response_model=schemas.CashTransaction)
def update_cash_transaction(transaction_id: int, transaction: schemas.CashTransactionUpdate, db: Session = Depends(get_db)):
    db_transaction = db.query(models.CashTransaction).filter(models.CashTransaction.id == transaction_id).first()
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Cash transaction not found")
    for key, value in transaction.dict(exclude_unset=True).items():
        setattr(db_transaction, key, value)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@app.delete("/cash-transactions/{transaction_id}")
def delete_cash_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = db.query(models.CashTransaction).filter(models.CashTransaction.id == transaction_id).first()
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Cash transaction not found")
    db.delete(db_transaction)
    db.commit()
    return {"message": "Cash transaction deleted successfully"}

# --- Bank Reconciliations ---

@app.post("/bank-reconciliations/", response_model=schemas.BankReconciliation)
def create_bank_reconciliation(reconciliation: schemas.BankReconciliationCreate, db: Session = Depends(get_db)):
    db_reconciliation = models.BankReconciliation(**reconciliation.dict())
    return create(db, db_reconciliation)

@app.get("/bank-reconciliations/", response_model=List[schemas.BankReconciliation])
def get_bank_reconciliations(db: Session = Depends(get_db)):
    return db.query(models.BankReconciliation).all()

@app.get("/bank-reconciliations/{reconciliation_id}", response_model=schemas.BankReconciliation)
def get_bank_reconciliation(reconciliation_id: int, db: Session = Depends(get_db)):
    db_reconciliation = db.query(models.BankReconciliation).filter(models.BankReconciliation.id == reconciliation_id).first()
    if not db_reconciliation:
        raise HTTPException(status_code=404, detail="Bank reconciliation not found")
    return db_reconciliation

@app.put("/bank-reconciliations/{reconciliation_id}", response_model=schemas.BankReconciliation)
def update_bank_reconciliation(reconciliation_id: int, reconciliation: schemas.BankReconciliationUpdate, db: Session = Depends(get_db)):
    db_reconciliation = db.query(models.BankReconciliation).filter(models.BankReconciliation.id == reconciliation_id).first()
    if not db_reconciliation:
        raise HTTPException(status_code=404, detail="Bank reconciliation not found")
    for key, value in reconciliation.dict(exclude_unset=True).items():
        setattr(db_reconciliation, key, value)
    db.commit()
    db.refresh(db_reconciliation)
    return db_reconciliation

@app.delete("/bank-reconciliations/{reconciliation_id}")
def delete_bank_reconciliation(reconciliation_id: int, db: Session = Depends(get_db)):
    db_reconciliation = db.query(models.BankReconciliation).filter(models.BankReconciliation.id == reconciliation_id).first()
    if not db_reconciliation:
        raise HTTPException(status_code=404, detail="Bank reconciliation not found")
    db.delete(db_reconciliation)
    db.commit()
    return {"message": "Bank reconciliation deleted successfully"}
