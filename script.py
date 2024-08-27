# script.py

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

# Path to your service account key file
GOOGLE_APPLICATION_CREDENTIALS = os.path.join(os.path.dirname(__file__), 'service_account_key.json')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

# Initialize the app with a service account, granting admin privileges
cred = credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS)
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore service
db = firestore.client()

# An enum for the category of the product, which is just toner and cleanser for now
class ProductCategory:
    CLEANSER = 'Cleanser'
    TONER = 'Toner'

# Function to clean up the Firestore database before each run
def clean_up_firestore():
    # Reference to the 'products' collection
    collection_ref = db.collection('products')
    
    # Get all documents in the collection
    docs = collection_ref.stream()
    
    # Delete each document
    for doc in docs:
        doc.reference.delete()

# Function to create test data in the Firestore database
def create_test_data():
    # Clean up Firestore collection before creating new data
    clean_up_firestore()

    # Loop through from 1 to 10 to create 10 products
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

    

if __name__ == "__main__":
    create_test_data()
    print("Test data created successfully.")