from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from core_db.db_utils import Base

class BankAccount(Base):
    __tablename__ = "bank_accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_name = Column(String, index=True)
    account_number = Column(String)
    bank_name = Column(String)
    currency = Column(String)

    transactions = relationship("CashTransaction", back_populates="bank_account")
    reconciliations = relationship("BankReconciliation", back_populates="bank_account")

class CashTransaction(Base):
    __tablename__ = "cash_transactions"

    id = Column(Integer, primary_key=True, index=True)
    bank_account_id = Column(Integer, ForeignKey("bank_accounts.id"))
    transaction_date = Column(Date)
    description = Column(String)
    amount = Column(Float)
    transaction_type = Column(String) # e.g., "deposit", "withdrawal"

    bank_account = relationship("BankAccount", back_populates="transactions")

class BankReconciliation(Base):
    __tablename__ = "bank_reconciliations"

    id = Column(Integer, primary_key=True, index=True)
    bank_account_id = Column(Integer, ForeignKey("bank_accounts.id"))
    reconciliation_date = Column(Date)
    bank_statement_balance = Column(Float)
    book_balance = Column(Float)
    
    bank_account = relationship("BankAccount", back_populates="reconciliations")
