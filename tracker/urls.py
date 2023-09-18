from django.urls import path
from .views import index, add_expense, edit_expense

urlpatterns = [
    path('', index, name="expense_list"),
    path('add/', add_expense, name='add_expense'),
    path('edit/<int:expense_id>/', edit_expense, name='edit_expense'),
    #
]
