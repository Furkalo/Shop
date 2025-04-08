from django.contrib import admin  # Import the Django admin interface
from django.urls import path, include  # Import path and include for URL routing
from django.conf import settings  # Import settings for accessing project configurations
from django.conf.urls.static import static  # Import static for serving media files during development

# URL patterns for routing requests to different views
urlpatterns = [
    path('admin/', admin.site.urls),  # Path for the Django admin interface
    path('', include('shop.urls', namespace='shop')),  # Main shop URLs (home page, product pages, etc.)
    path('accounts/', include('accounts.urls', namespace='accounts')),  # User authentication URLs (login, registration, etc.)
    path('cart/', include('cart.urls', namespace='cart')),  # Shopping cart URLs (add/remove items, view cart, etc.)
    path('orders/', include('orders.urls', namespace='orders')),  # Orders-related URLs (order placement, history, etc.)
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),  # Admin or user dashboard URLs (for managing content)
]

# If the project is in DEBUG mode, add static URL patterns to serve media files (like images) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
