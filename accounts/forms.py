from django import forms  # Import Django forms module

from .models import User  # Import User model from the app's models

# Form for user login
class UserLoginForm(forms.Form):
    email = forms.EmailField(  # Email field with custom widget for styling
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'})
    )
    password = forms.CharField(  # Password field with custom widget for styling
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'})
    )

# Form for user registration
class UserRegistrationForm(forms.Form):
    email = forms.EmailField(  # Email field with custom widget
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'})
    )
    full_name = forms.CharField(  # Full name field with custom widget
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'full name'})
    )
    password = forms.CharField(  # Password field with custom widget
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'})
    )

# Form for manager login
class ManagerLoginForm(forms.Form):
    email = forms.EmailField(  # Email field for manager login
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'})
    )
    password = forms.CharField(  # Password field for manager login
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'})
    )

# Form for editing user profile
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User  # The form is tied to the User model
        fields = ['full_name', 'email']  # Fields that can be edited
