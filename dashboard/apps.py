from django.apps import AppConfig

# Configuration class for the 'dashboard' app
class DashboardConfig(AppConfig):
    # Default auto field for models in this app
    default_auto_field = 'django.db.models.BigAutoField'

    # Name of the app
    name = 'dashboard'
