from django.urls import path
from .views import (index, expense_list, paginated_view, add_expense, edit_expense, ExpenseDetailView,
                    ExpenseDeleteView)

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name="home"),
    path('expense/', expense_list, name="expense_list"),
    path('expenses/', paginated_view, name="paginated"),
    path('add/', add_expense, name='add_expense'),
    path('expenses/<int:pk>/',
         ExpenseDetailView.as_view(), name='expense_detail'),

    path('edit/<int:expense_id>/', edit_expense, name='edit_expense'),
    path('expense/delete/<int:pk>/', ExpenseDeleteView.as_view(),
         name='delete_expense'),


]
