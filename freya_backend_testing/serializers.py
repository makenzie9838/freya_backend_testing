# freya_backend_testing/serializers.py
from rest_framework import serializers
from freya_backend_testing.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'