# freya_backend_testing/firebase_config.py
import firebase_admin
from firebase_admin import credentials, firestore
import os

GOOGLE_APPLICATION_CREDENTIALS = "/Users/mackenzieeng/headstarter-fellowship/freya_backend_testing/freya_backend_testing/service_account_key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS

cred = credentials.Certificate(GOOGLE_APPLICATION_CREDENTIALS)
firebase_admin.initialize_app(cred)

db = firestore.client()