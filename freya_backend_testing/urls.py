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
    FilterProductsByCategory,
    FilterProductsByCategoryAndIngredient,
    FilterOutProductsByCategoryAndIngredient
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filter_by_category/', FilterProductsByCategory.as_view(), name='filter_by_category'),
    path('filter_by_category_and_ingredient/', FilterProductsByCategoryAndIngredient.as_view(), name='filter_by_category_and_ingredient'),
    path('filter_out_by_category_and_ingredient/', FilterOutProductsByCategoryAndIngredient.as_view(), name='filter_out_by_category_and_ingredient'),
]
