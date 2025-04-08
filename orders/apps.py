from django.apps import AppConfig  # Import AppConfig class from Django to configure the application

# Define a configuration class for the Orders app
class OrdersConfig(AppConfig):
    # Set the default primary key field type for the app's models
    default_auto_field = 'django.db.models.BigAutoField'

    # Specify the name of the application within Django
    name = 'orders'
