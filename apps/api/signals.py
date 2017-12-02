from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Api
import pyrebase

config = {
  "apiKey": settings.FIREBASE_API_KEY,
  "authDomain": settings.FIREBASE_DOMAIN,
  "databaseURL": settings.FIREBASE_DATABASE_URL,
  "storageBucket": settings.FIREBASE_BUCKET
}

firebase = pyrebase.initialize_app(config)


@receiver(post_save, sender=Api)
def send_data(sender, instance, created, **kwargs):
    data = {
        'image': instance.publication_file.url,
        'date': instance.date,
        'final_date': instance.final_date
    }
    db = firebase.database()
    db.child('info').push(data)
