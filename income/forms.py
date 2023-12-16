from django import forms
from .models import Income
from datetime import date


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'source', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the default value for the 'date' field to the current date
        self.fields['date'].initial = date.today()
