from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, User
from .serializers import ProductSerializer, UserSerializer
from django.shortcuts import get_object_or_404

class SearchAndFilterProducts(APIView):
    def get(self, request, format=None):
        # Get query parameters
        search_text = request.query_params.get('text', None)
        category = request.query_params.get('categories', None)
        ingredient = request.query_params.get('ingredients', None)
        
        # Start with all products
        products = Product.objects.all()

        # Filter by search text if provided
        if search_text:
            products = products.filter(name__icontains=search_text)

        # Filter by category if provided
        if category:
            products = products.filter(category__icontains=category)

        # Filter by ingredient if provided
        if ingredient:
            products = products.filter(ingredients__icontains=ingredient)

        # Serialize and return the products
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class GetProduct(APIView):
    def get(self, request, product_id, format=None):
        # Fetch the product by ID
        product = get_object_or_404(Product, pk=product_id)

        # Serialize and return the product
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
class GetUser(APIView):
    def get(self, request, user_id, format=None):
        # Fetch the user by ID
        user = get_object_or_404(User, pk=user_id)

        # Serialize and return the user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    