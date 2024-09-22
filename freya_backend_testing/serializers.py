# freya_backend_testing/serializers.py
from rest_framework import serializers
from freya_backend_testing.models import Product, User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'