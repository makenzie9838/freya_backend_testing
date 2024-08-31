from freya_backend_testing.models import Product

class ProductCategory:
    CLEANSER = 'Cleanser'
    TONER = 'Toner'

def create_test_data():
    # Clear existing data
    Product.objects.all().delete()

    # Insert new data
    for i in range(1, 11):
        Product.objects.create(
            name=f'Product {i}',
            image=f'https://www.example.com/image_{i}.png',
            url=f'https://www.example.com/product_{i}',
            ingredients=f'Ingredient {i}',
            estimated_price=i * 10,
            category=ProductCategory.CLEANSER if i % 2 == 0 else ProductCategory.TONER,
            skin_tags=f'Skin Tag {i}',
        )