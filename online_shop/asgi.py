import os

from django.core.asgi import get_asgi_application

# Set the default settings module for the 'asgi' command to 'online_shop.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_shop.settings')

# Get the ASGI application for the project
application = get_asgi_application()
