from django.apps import AppConfig

class CartConfig(AppConfig):
    # The default field type for auto-generated fields like primary keys
    default_auto_field = 'django.db.models.BigAutoField'

    # The name of the app (used for internal Django purposes)
    name = 'cart'
