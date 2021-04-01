from django import forms
from .models import *

class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','middle_name','last_name']

class SavingsCreateForm(forms.ModelForm):
    class Meta:
        model = Savings
        fields = ['person','amount','date']
