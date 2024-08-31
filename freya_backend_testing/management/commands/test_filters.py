from django.core.management.base import BaseCommand
from freya_backend_testing.models import Product
from freya_backend_testing.database_utils import filter_products_by_ingredient, filter_out_products_that_have_ingredient

class Command(BaseCommand):
    help = 'Test filter functions for products.'

    def handle(self, *args, **kwargs):
        # Ensure test data is created
        from freya_backend_testing.database_utils import create_test_data
        create_test_data()
        
        # Test filtering by ingredient
        ingredient = 'Ingredient 1'
        filtered_products = filter_products_by_ingredient(ingredient)
        self.stdout.write(self.style.SUCCESS(f'Products with ingredient "{ingredient}":'))
        for product in filtered_products:
            self.stdout.write(f'{product.name} - {product.ingredients}')

        # Test filtering out products by ingredient
        filtered_out_products = filter_out_products_that_have_ingredient(ingredient)
        self.stdout.write(self.style.SUCCESS(f'Products without ingredient "{ingredient}":'))
        for product in filtered_out_products:
            self.stdout.write(f'{product.name} - {product.ingredients}')