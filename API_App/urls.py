from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from API_App import views

urlpatterns = [
    path('', views.Covid_19.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)