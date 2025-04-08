from django.contrib import admin

# Import the models to be registered in the admin interface
from .models import Category, Product

# Register the Category model to make it available in the admin interface
admin.site.register(Category)

# Register the Product model to make it available in the admin interface
admin.site.register(Product)
