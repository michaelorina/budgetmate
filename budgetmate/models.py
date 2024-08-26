from django.db import models

# Create your models here.

class Budget(models.Model):
    income = models.DecimalField(max_digits=10, decimal_places=2)
    savings = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)
    investments = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'Budget for {self.income}'
