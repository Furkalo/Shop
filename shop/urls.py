from django.urls import path

from shop import views

# Defining the app name for namespacing URLs
app_name = "shop"

# URL patterns for the shop application
urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('<slug:slug>', views.product_detail, name='product_detail'),
	path('add/favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
	path('remove/favorites/<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
	path('favorites/', views.favorites, name='favorites'),
	path('search/', views.search, name='search'),
	path('filter/<slug:category_slug>/', views.filter_by_price_with_category, name='filter_by_category'),
	path('filter/', views.filter_by_price, name='filter_by_price'),
]


