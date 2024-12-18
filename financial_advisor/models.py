from django.db import models

class FinancialAdvice(models.Model):
    prompt = models.TextField()
    response = models.TextField()

class AdviceCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
