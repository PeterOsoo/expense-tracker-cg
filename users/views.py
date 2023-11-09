from django.shortcuts import render, redirect
from .decorators import redirect_logged_in_user

from django.contrib import messages
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm


# Create your views here.


@redirect_logged_in_user
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('expense_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@redirect_logged_in_user
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
