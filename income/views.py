from django.shortcuts import render, redirect
from .models import Income
from .forms import IncomeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    return render(request, 'income/income_list.html', {'incomes': incomes})


def new_list(request):
    return render(request, 'income/list.html', {})


@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            amount = form.cleaned_data.get('amount')
            source = form.cleaned_data.get('source')
            messages.success(
                request, f'KES {amount} from {source} received & updated!')
            return redirect('income_list')
    else:
        form = IncomeForm()
    return render(request, 'income/add_income.html', {'form': form})
