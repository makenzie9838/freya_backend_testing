# freya_backend_testing/firestore_utils.py
from .firebase_config import db
from firebase_admin import firestore

class ProductCategory:
    CLEANSER = 'Cleanser'
    TONER = 'Toner'

def clean_up_firestore():
    collection_ref = db.collection('products')
    docs = collection_ref.stream()
    for doc in docs:
        doc.reference.delete()

def create_test_data():
    clean_up_firestore()
    for i in range(1, 11):
        doc_ref = db.collection('products').document(f'product_{i}')
        doc_ref.set({
            'id': i,
            'name': f'Product {i}',
            'image': f'https://www.example.com/image_{i}.png',
            'url': f'https://www.example.com/product_{i}',
            'ingredients': f'Ingredient {i}',
            'estimated_price': i * 10,
            'category': ProductCategory.CLEANSER if i % 2 == 0 else ProductCategory.TONER,
            'skin_tags': f'Skin Tag {i}',
            'created_at': firestore.SERVER_TIMESTAMP
        })