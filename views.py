from django.shortcuts import render
from .models import News
from django.db.models import Q

def index(request):
    news_list = News.objects.all()
    return render(request, 'news/index.html', {'news_list': news_list})

def search(request):
    query = request.GET.get('q')
    city = request.GET.get('city')
    state = request.GET.get('state')

    results = News.objects.all()

    if query:
        results = results.filter(Q(title__icontains=query) | Q(content__icontains=query))
    if city:
        results = results.filter(city__icontains=city)
    if state:
        results = results.filter(state__icontains=state)

    return render(request, 'news/search_results.html', {'results': results})
