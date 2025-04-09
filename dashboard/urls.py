from django.urls import path

from dashboard import views

# Define the app name for namespacing URLs in the dashboard app
app_name = 'dashboard'

urlpatterns = [
    # Product-related URLs
    path('products', views.products, name='products'),  # View all products
    path('products/delete/<int:id>', views.delete_product, name='delete_product'),  # Delete a specific product by ID
    path('products/edit/<int:id>', views.edit_product, name='edit_product'),  # Edit a specific product by ID

    # Order-related URLs
    path('orders', views.orders, name='orders'),  # View all orders
    path('orders/detail/<int:id>', views.order_detail, name='order_detail'),  # View detailed order information by ID

    # URLs for adding a product and category
    path('add-product/', views.add_product, name='add_product'),  # Add a new product
    path('add-category/', views.add_category, name='add_category'),  # Add a new category

    # Category-related URLs
    path('category/delete/<int:id>', views.delete_category, name='delete_category'),  # Delete a specific category by ID
    path('category/edit/<int:id>', views.edit_category, name='edit_category'),  # Edit a specific category by ID
    path('categories', views.categories, name='categories')  # View all categories
]
