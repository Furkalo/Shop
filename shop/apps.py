from django.apps import AppConfig

# Define the configuration class for the 'shop' app
class ShopConfig(AppConfig):
    # Set the default type of auto-generated primary key field (BigAutoField is a large integer type)
    default_auto_field = 'django.db.models.BigAutoField'

    # Define the name of the app. This is used by Django to reference the app in various parts of the project
    name = 'shop'
