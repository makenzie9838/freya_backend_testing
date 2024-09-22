from freya_backend_testing.models import Product, User

class ProductCategory:
    CLEANSER = 'Cleanser'
    TONER = 'Toner'

class SkinType:
    DRY = 'Dry'
    OILY = 'Oily'
    COMBINATION = 'Combination'
    SENSITIVE = 'Sensitive'

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
    
    for i in range(1, 11):
        User.objects.create(
            name=f'User {i}',
            email =f'testemail{i}@gmail.com',
            telephone =f'123456789{i}',
            subscriptionStatus = True if i % 2 == 0 else False,
            # random skin type
            skinType = SkinType.DRY if i % 4 == 0 else SkinType.OILY if i % 3 == 0 else SkinType.COMBINATION if i % 2 == 0 else SkinType.SENSITIVE,
            photos = f'https://www.example.com/image_{i}.png',
            # set it to random time
            created_at = f'2022-01-0{i}T00:00:00Z'
        )
