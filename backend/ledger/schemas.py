from pydantic import BaseModel
from typing import List

class AccountCreate(BaseModel):
    name: str
    account_type: str

class Account(AccountCreate):
    id: int

class TransactionCreate(BaseModel):
    date: str
    description: str

class Transaction(TransactionCreate):
    id: int

class JournalEntryCreate(BaseModel):
    transaction_id: int
    account_id: int
    amount: float
    entry_type: str

class JournalEntry(JournalEntryCreate):
    id: int
