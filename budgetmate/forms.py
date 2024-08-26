from django import forms
from decimal import Decimal

class IncomeForm(forms.Form):
    income = forms.DecimalField(max_digits=10, decimal_places=2, label='Income')
    
    def clean_income(self):
        income = self.cleaned_data['income']
        if income <= Decimal('0.00'):
            raise forms.ValidationError("Income must be greater than zero.")
        return income
