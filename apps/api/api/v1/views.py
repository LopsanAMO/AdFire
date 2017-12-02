from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import ApiSerializer
from api.models import Api


class APIView(generics.ListCreateAPIView):
	queryset = Api.objects.all()
	serializer_class = ApiSerializer
