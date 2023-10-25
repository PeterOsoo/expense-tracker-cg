from django.urls import path
from .views import (index, expense_list, add_expense, edit_expense, expense_detail,
                    ExpenseDeleteView, register, login, logout_view)

urlpatterns = [
    path('', index, name="home"),
    path('expense/', expense_list, name="expense_list"),
    path('add/', add_expense, name='add_expense'),
    path('expenses/<int:expense_id>/',
         expense_detail, name='expense_detail'),

    path('edit/<int:expense_id>/', edit_expense, name='edit_expense'),
    path('expenses/delete/<int:pk>/', ExpenseDeleteView.as_view(),
         name='delete_expense'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),

]
