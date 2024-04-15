from django.urls import path
from .views import income_list, add_income, new_list

urlpatterns = [
    path('', income_list, name='income_list'),
    path('add/', add_income, name='add_income'),
    path('list/', new_list, name='new_list'),
]
