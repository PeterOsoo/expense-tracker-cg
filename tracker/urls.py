from django.urls import path
from .views import index, add_expense, edit_expense, ExpenseDeleteView, register

urlpatterns = [
    path('', index, name="expense_list"),
    path('add/', add_expense, name='add_expense'),
    path('edit/<int:expense_id>/', edit_expense, name='edit_expense'),
    path('expenses/delete/<int:pk>/', ExpenseDeleteView.as_view(),
         name='delete_expense'),
    path('register/', register, name='register'),

]
