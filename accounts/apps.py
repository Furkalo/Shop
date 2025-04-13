"""
from django.apps import AppConfig

# Define the configuration for the 'accounts' app
class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Set default primary key type
    name = 'accounts'  # Define the name of the app
"""

from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from accounts.views import create_manager
        create_manager()
