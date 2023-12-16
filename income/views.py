from django.shortcuts import render, redirect
from .models import Income
from .forms import IncomeForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    return render(request, 'income/income_list.html', {'incomes': incomes})


@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('income_list')
    else:
        form = IncomeForm()
    return render(request, 'income/add_income.html', {'form': form})
