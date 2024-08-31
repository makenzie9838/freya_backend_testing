from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.URLField(max_length=1024)
    url = models.URLField(max_length=1024)
    ingredients = models.TextField()
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    skin_tags = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)