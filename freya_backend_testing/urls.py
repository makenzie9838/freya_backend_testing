from django.contrib import admin
from django.urls import path, include
from .views import (
    SearchAndFilterProducts,
    GetProduct,
    GetUser 
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Search and/or Filter Products Endpoint
    path('products/', SearchAndFilterProducts.as_view(), name='search_and_filter_products'),
    
    # Get Product by ID Endpoint
    path('product/<int:product_id>/', GetProduct.as_view(), name='get_product'),

    # Get User by ID Endpoint
    path('user/<int:user_id>/', GetUser.as_view(), name='get_user'),

    path('api/', include('djoser.urls')),

    path('api/', include('djoser.urls.jwt')),
]
