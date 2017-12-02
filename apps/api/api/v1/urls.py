from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import APIView

urlpatterns = [
    url(r'^send_images/', csrf_exempt(APIView.as_view())),
]
