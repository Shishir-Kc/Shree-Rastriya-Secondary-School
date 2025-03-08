import firebase_admin 
from firebase_admin import credentials

cred = credentials.Certificate('/home/mrkc/Shree-Rastriya-Secondary-School/Shree_Rastriya_Secondary_School/cred/shree-rastriya-mavi-firebase-adminsdk-fbsvc-e836b2d8d5.json')
firebase_admin.initialize_app(cred)