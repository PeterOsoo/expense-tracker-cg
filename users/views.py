from django.shortcuts import render, redirect
from .decorators import redirect_logged_in_user

from django.contrib import messages
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm


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
            messages.success(
                request, f'Account created successfully for {username}! You have been logged in!')
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


def logout_confirmation(request):
    if not request.user.is_authenticated:
        return render(request, 'users/logout_confirmation.html')
    else:
        # If the user is logged in, log them out
        logout(request)
        return render(request, 'users/logout_confirmation.html')


@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
