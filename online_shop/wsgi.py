import os  # Import the os module to interact with the operating system

from django.core.wsgi import get_wsgi_application  # Import WSGI application for serving the Django app

from accounts.views import create_manager  # Import the create_manager function from the accounts views

# Set the default settings module for the Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_shop.settings')

# Create a user with the 'manager' role by calling the create_manager function
create_manager()

# Get the WSGI application, which is used to run the Django app in a production environment
application = get_wsgi_application()
