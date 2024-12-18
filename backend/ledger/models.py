from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=255) # e.g., 'Asset', 'Liability', 'Equity', 'Revenue', 'Expense'

class Transaction(models.Model):
    date = models.DateField()
    description = models.TextField()

class JournalEntry(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    entry_type = models.CharField(max_length=255) # 'Debit' or 'Credit'
