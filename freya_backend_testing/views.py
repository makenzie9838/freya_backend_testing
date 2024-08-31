from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from freya_backend_testing.models import Product
from freya_backend_testing.serializers import ProductSerializer

class FilterProductsByCategory(APIView):
    def get(self, request, format=None):
        category = request.query_params.get('category', None)
        if category:
            products = Product.objects.filter(category=category)
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class FilterProductsByCategoryAndIngredient(APIView):
    def get(self, request, format=None):
        category = request.query_params.get('category', None)
        ingredient = request.query_params.get('ingredient', None)
        
        if category and ingredient:
            # Filter by exact match on ingredient
            products = Product.objects.filter(category=category, ingredients__exact=ingredient)
        else:
            products = Product.objects.all()
            
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class FilterOutProductsByCategoryAndIngredient(APIView):
    def get(self, request, format=None):
        category = request.query_params.get('category', None)
        ingredient = request.query_params.get('ingredient', None)
        
        if category and ingredient:
            # Exclude products with the specified ingredient in the given category
            products = Product.objects.filter(category=category).exclude(ingredients__icontains=ingredient)
        elif category:
            # If only category is provided, exclude products with the specified ingredient
            products = Product.objects.filter(category=category)
        elif ingredient:
            # If only ingredient is provided, exclude products with the specified ingredient across all categories
            products = Product.objects.exclude(ingredients__icontains=ingredient)
        else:
            # If neither category nor ingredient is provided, return all products
            products = Product.objects.all()
            
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)