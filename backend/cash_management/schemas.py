from datetime import date
from pydantic import BaseModel
from typing import Optional

class BankAccountBase(BaseModel):
    account_name: str
    account_number: str
    bank_name: str
    currency: str

class BankAccountCreate(BankAccountBase):
    pass

class BankAccountUpdate(BaseModel):
    account_name: Optional[str] = None
    account_number: Optional[str] = None
    bank_name: Optional[str] = None
    currency: Optional[str] = None

class BankAccount(BankAccountBase):
    id: int

    class Config:
        orm_mode = True

class CashTransactionBase(BaseModel):
    bank_account_id: int
    transaction_date: date
    description: str
    amount: float
    transaction_type: str

class CashTransactionCreate(CashTransactionBase):
    pass

class CashTransactionUpdate(BaseModel):
    transaction_date: Optional[date] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    transaction_type: Optional[str] = None

class CashTransaction(CashTransactionBase):
    id: int

    class Config:
        orm_mode = True

class BankReconciliationBase(BaseModel):
    bank_account_id: int
    reconciliation_date: date
    bank_statement_balance: float
    book_balance: float

class BankReconciliationCreate(BankReconciliationBase):
    pass

class BankReconciliationUpdate(BaseModel):
    reconciliation_date: Optional[date] = None
    bank_statement_balance: Optional[float] = None
    book_balance: Optional[float] = None

class BankReconciliation(BankReconciliationBase):
    id: int

    class Config:
        orm_mode = True
