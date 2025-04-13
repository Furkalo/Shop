import os  # Import the os module to interact with the operating system

from django.core.wsgi import get_wsgi_application  # Import WSGI application for serving the Django app


# Set the default settings module for the Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_shop.settings')

# Get the WSGI application, which is used to run the Django app in a production environment
application = get_wsgi_application()


"""

from accounts.views import create_manager  # Import the create_manager function from the accounts views

# Create a user with the 'manager' role by calling the create_manager function
create_manager()
"""