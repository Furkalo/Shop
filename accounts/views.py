from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import UserRegistrationForm, UserLoginForm, ManagerLoginForm, EditProfileForm
from accounts.models import User


def create_manager():
    """
    Function to create a manager user if not already exists.
    This function should be executed once on startup in `urls.py` (e.g., using a signal or during the app initialization).
    """
    if not User.objects.filter(email="manager@example.com").first():
        user = User.objects.create_user(
            "manager@example.com", 'shop manager', 'managerpass1234'
        )
        # Give this user manager role
        user.is_manager = True
        user.save()


def manager_login(request):
    """Handles the manager login process."""
    if request.method == 'POST':
        form = ManagerLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['password']
            )
            if user is not None and user.is_manager:  # Check if the user is a manager
                login(request, user)
                return redirect('dashboard:products')  # Redirect to manager dashboard
            else:
                messages.error(
                    request, 'Username or password is incorrect', 'danger'
                )
                return redirect('accounts:manager_login')
    else:
        form = ManagerLoginForm()
    context = {'form': form}
    return render(request, 'manager_login.html', context)


def user_register(request):
    """Handles user registration."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['email'], data['full_name'], data['password']
            )
            return redirect('accounts:user_login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    context = {'title': 'Signup', 'form': form}
    return render(request, 'register.html', context)


def user_login(request):
    """Handles user login."""
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('shop:home_page')  # Redirect to homepage after successful login
            else:
                messages.error(
                    request, 'Username or password is incorrect', 'danger'
                )
                return redirect('accounts:user_login')
    else:
        form = UserLoginForm()
    context = {'title': 'Login', 'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    """Logs out the user and redirects to login page."""
    logout(request)
    return redirect('accounts:user_login')


def edit_profile(request):
    """Handles editing of user profile information."""
    form = EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your profile has been updated', 'success')
        return redirect('accounts:edit_profile')  # Redirect back to edit profile page
    else:
        form = EditProfileForm(instance=request.user)
    context = {'title': 'Edit Profile', 'form': form}
    return render(request, 'edit_profile.html', context)
