from django.urls import path
from django.http import JsonResponse
from . import views

urlpatterns = [
    path('', lambda r: JsonResponse({"message":"gut"}), name='health check'),
    path('news/', views.news_with_images, name='news_with_images'),
]