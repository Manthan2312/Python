import firebase_admin
from firebase_admin import credentials, db

if not firebase_admin._apps:
    cred = credentials.Certificate("C:\\Users\\manthan patel\\downloads\\newproject-e9b7c-firebase-adminsdk-fbsvc-7835270b92.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://newproject-e9b7c-default-rtdb.firebaseio.com/'
    })

ref = db.reference('users')
ref.update({
    "name": "Manthan Patel",
    "mobile": "8140519426",
    "dept": "M-COM",
})