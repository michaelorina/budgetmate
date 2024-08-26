from django.test import TestCase
from decimal import Decimal
from .models import Budget
from .views import calculate_budget

# Create your tests here.

class BudgetCalculationTest(TestCase):
    def test_calculate_budget(self):
        income = Decimal('1000.00')
        savings, expenses, investments = calculate_budget(income)
        self.assertEqual(savings, Decimal('200.00'))
        self.assertEqual(expenses, Decimal('500.00'))
        self.assertEqual(investments, Decimal('300.00'))
        
    def test_budget_creation(self):
        income = Decimal('1000')
        savings, expenses, investments = calculate_budget(income)
        budget = Budget.objects.create(income=income, savings=savings, expenses=expenses, investments=investments)
        self.assertEqual(budget.income, income)
        self.assertEqual(budget.savings, savings)
        self.assertEqual(budget.expenses, expenses)
        self.assertEqual(budget.investments, investments)
