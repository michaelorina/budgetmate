from django.shortcuts import render
from .forms import IncomeForm
from .models import Budget
from decimal import Decimal

# Create your views here.

def calculate_budget(income):
    if income <= 0:
        raise ValueError("Income must be greater than zero.")
    savings_pct = Decimal('0.20')
    expenses_pct = Decimal('0.50')
    investments_pct = Decimal('0.30')

    savings = income * savings_pct
    expenses = income * expenses_pct
    investments = income * investments_pct

    return savings, expenses, investments

def budget_view(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            try:
                income = form.cleaned_data['income']
                savings, expenses, investments = calculate_budget(income)
                budget = Budget.objects.create(income=income, savings=savings, expenses=expenses, investments=investments)
                context = {'budget': budget}
                return render(request, 'budgetmate/result.html', context)
            except ValueError as e:
                messages.error(request, str(e))
    else:
        form = IncomeForm()
    return render(request, 'budgetmate/input.html', {'form': form})
