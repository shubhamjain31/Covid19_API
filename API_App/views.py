from django.shortcuts import render
from API_App.serializers import Covid19Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from API_App import worldData

# Create your views here.

class Covid_19(APIView):
	def get(self, request):
		covid19_data =  worldData.covid_data()
		results = Covid19Serializer(covid19_data, many=True).data
		return Response(results)