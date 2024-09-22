"""
URL configuration for freya_backend_testing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
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
]
