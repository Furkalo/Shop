from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.user_register, name='user_register'),  # User registration
    path('login/', views.user_login, name='user_login'),  # User login
    path('login/manager/', views.manager_login, name='manager_login'),  # Manager login
    path('logout/', views.user_logout, name='user_logout'),  # User logout
    path('profile/edit', views.edit_profile, name='edit_profile'),  # Edit user profile
    path(
        'password-reset/',  # Password reset request
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',  # Template for password reset
            success_url=reverse_lazy('accounts:password_reset_done'),  # Redirect after success
            email_template_name='email_template.html'  # Email template for reset instructions
        ),
        name='password_reset'
    ),
    path(
        'password-reset/done',  # Confirmation after password reset request
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html',  # Template for password reset done
        ),
        name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',  # URL for password reset confirmation
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html',  # Template for reset confirmation
            success_url=reverse_lazy('accounts:password_reset_complete'),  # Redirect after success
        ),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete/',  # Confirmation after password reset completion
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html',  # Template for reset complete
        ),
        name='password_reset_complete'
    ),
]
