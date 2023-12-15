from django.urls import path
from .views import income_list, add_income

urlpatterns = [
    path('income/', income_list, name='income_list'),
    path('income/add/', add_income, name='add_income'),
]
