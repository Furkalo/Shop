from django.contrib import admin

from .models import User

# Register the User model to make it accessible in the Django admin interface
admin.site.register(User)
