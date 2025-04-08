from django.apps import AppConfig

# Define the configuration for the 'accounts' app
class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Set default primary key type
    name = 'accounts'  # Define the name of the app

