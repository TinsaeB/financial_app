from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from core_db.db_utils import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    account_type = Column(String)  # e.g., 'Asset', 'Liability', 'Equity', 'Revenue', 'Expense'

    transactions = relationship("Transaction", secondary="journal_entries", back_populates="accounts")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    description = Column(String)

    accounts = relationship("Account", secondary="journal_entries", back_populates="transactions")
    journal_entries = relationship("JournalEntry", back_populates="transaction")

class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, ForeignKey("transactions.id"))
    account_id = Column(Integer, ForeignKey("accounts.id"))
    amount = Column(Float)
    entry_type = Column(String)  # 'Debit' or 'Credit'

    transaction = relationship("Transaction", back_populates="journal_entries")
    account = relationship("Account")
