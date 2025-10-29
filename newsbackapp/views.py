from django.http import JsonResponse
from django.shortcuts import render
from .models import News

def news_with_images(request):
    news_items = News.objects.prefetch_related('images').all()
    
    data = []
    for news in news_items:
        data.append({
            'id': news.id,
            'title': news.title,
            'text': news.text,
            'created_at': news.created_at,
            'updated_at': news.updated_at,
            'images': [{'id': image.id, 'url': image.image.url if image.image else ''} for image in news.images.all()]
        })

    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})