from pydantic import BaseModel
from typing import List

class AccountCreate(BaseModel):
    name: str
    account_type: str

class Account(AccountCreate):
    id: int

from datetime import date
from pydantic import BaseModel
from typing import List

class AccountCreate(BaseModel):
    name: str
    account_type: str

class Account(AccountCreate):
    id: int

    class Config:
        orm_mode = True

class TransactionCreate(BaseModel):
    date: date
    description: str

class Transaction(TransactionCreate):
    id: int

    class Config:
        orm_mode = True

class JournalEntryCreate(BaseModel):
    transaction_id: int
    account_id: int
    amount: float
    entry_type: str

class JournalEntry(JournalEntryCreate):
    id: int

    class Config:
        orm_mode = True
