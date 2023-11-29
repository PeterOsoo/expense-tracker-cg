from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.views.generic.edit import DeleteView
from django.utils.decorators import method_decorator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime


from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView


from django.contrib import messages


from .models import Expense
from .forms import ExpenseForm


def index(request):
    return render(request, 'home.html', {})


@login_required
def expense_list(request):
    # expenses = Expense.objects.all()
    # expenses = Expense.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user).order_by('-date')

    return render(request, 'tracker/expense_list.html', {'expenses': expenses})


@login_required
def paginated_view(request):
    queryset = Expense.objects.all()

    # Group expenses by month
    expenses_by_month = {}
    for expense in queryset:
        month_year = expense.date.strftime('%B %Y')
        if month_year not in expenses_by_month:
            expenses_by_month[month_year] = []
        expenses_by_month[month_year].append(expense)

    # Sort months in descending order
    sorted_months = sorted(expenses_by_month.keys(), reverse=True)

    # Paginate based on months
    # Each page contains expenses for a specific month
    paginator = Paginator(sorted_months, 1)

  # Get the latest month by default
    current_month_year = datetime.now().strftime('%B %Y')
    default_page_index = sorted_months.index(current_month_year)
    default_page = paginator.page(
        (default_page_index // paginator.per_page) * paginator.per_page + 1)

    page = request.GET.get('page', default_page)

    try:
        # Get the month for the current page
        month_year = paginator.page(page).object_list[0]
        months = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        month_year = paginator.page(1).object_list[0]
        months = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
        month_year = paginator.page(paginator.num_pages).object_list[0]
        months = paginator.page(paginator.num_pages)

    # Retrieve expenses for the selected month
    expenses = expenses_by_month.get(month_year, [])

    return render(request, 'tracker/paginated.html', {'months': months, 'expenses': expenses})


# detail view

class ExpenseDetailView(DetailView):
    model = Expense


def expense_detail(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    return render(request, 'tracker/expense_detail.html', {'expense': expense})


@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'tracker/expense_form.html', {'form': form})


@login_required
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    # Check if the logged-in user is the owner of the expense
    if expense.user != request.user:
        # Handle unauthorized access, e.g., redirect or display an error message
        # Redirect to the expense list or a suitable page
        return redirect('expense_list')

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'tracker/expense_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'tracker/expense_confirm_delete.html'
    success_url = reverse_lazy('expense_list')

    def get(self, request, *args, **kwargs):
        expense = self.get_object()
        if expense.user != self.request.user:
            # Redirect to the expense list for unauthorized users
            return redirect('expense_list')
        return super().get(request, *args, **kwargs)
