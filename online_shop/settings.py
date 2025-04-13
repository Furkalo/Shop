import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR is the root directory of your project, used for constructing other paths.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY is used for cryptographic signing, and it should not be exposed in production.
SECRET_KEY = 'django-insecure-kr1p-zj6!vss$(xd2f7vk8nw*3g@-ao92zzg8^@u!mj(l#s)+i'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG should be set to False in production for security reasons.
DEBUG = False

# ALLOWED_HOSTS defines a list of valid host/domain names for your Django site.
# It is used to prevent HTTP Host header attacks.
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # Default Django apps for admin, authentication, sessions, etc.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'crispy_forms', # For rendering forms using Bootstrap4 styles

    # Custom apps
    'accounts.apps.AccountsConfig',  # Accounts app for user management
    'cart.apps.CartConfig',          # Cart app for shopping cart functionality
    'orders.apps.OrdersConfig',      # Orders app for order management
    'shop.apps.ShopConfig',          # Shop app for product and category management
    'dashboard.apps.DashboardConfig',  # Dashboard app for administrative interface

]

# Middleware for various security and request processing tasks
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration for the project
ROOT_URLCONF = 'online_shop.urls'

# Template settings for rendering HTML pages
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # List of directories where templates are stored (empty in this case)
        'APP_DIRS': True,  # Django will look for templates in each app's 'templates' directory
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'online_shop.context_processors.return_cart',  # Custom context processor for cart count
                'online_shop.context_processors.return_categories',  # Custom context processor for categories
            ],
        },
    },
]

# WSGI application for the project
WSGI_APPLICATION = 'online_shop.wsgi.application'


# Database settings for using SQLite database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite database engine
        'NAME': BASE_DIR / 'db.sqlite3',  # Database file stored in the base directory
    }
}

# Custom user model for the accounts app
AUTH_USER_MODEL = 'accounts.User'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

# Password validation settings for enhancing security
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'media'),   # your directory with additional static files
]

# Localization settings for internationalization
LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'UTC'  # Time zone for the project (Coordinated Universal Time)

USE_I18N = True  # Enable internationalization (for multi-language support)
USE_TZ = True  # Enable timezone-aware datetime objects


# Static files (CSS, JavaScript, Images)
# Settings for serving static files like CSS and JavaScript
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # може поламатись

# Directory for storing uploaded media files (e.g., user-uploaded images, documents)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'  # URL to access media files from the browser

# Default primary key field type for model auto-increment
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Crispy forms configuration for rendering forms with Bootstrap 4 styles
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Login URL for authentication redirects
LOGIN_URL = 'accounts:user_login'


# Email backend configuration for sending emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Use SMTP to send emails
EMAIL_HOST = 'smtp.gmail.com'  # Gmail SMTP server
EMAIL_PORT = 587  # Port for sending email via TLS
EMAIL_USE_SSL = False  # Don't use SSL
EMAIL_USE_TLS = True  # Use TLS for secure email sending
EMAIL_HOST_USER = 'username@example.com'  # Sender's email address
EMAIL_HOST_PASSWORD = 'your-password'  # Sender's email password