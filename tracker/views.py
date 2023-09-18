from django.shortcuts import render
from .models import Expense

# Create your views here.


def index(request):
    expenses = Expense.objects.all()
    return render(request, 'home.html', {'expenses': expenses})
