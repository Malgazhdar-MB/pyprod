from django.shortcuts import render, get_object_or_404
from .models import News, Category
from .forms import NewsForm

def index(request):
    news = News.objects.filter(is_published=True)
    con = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=con)

def category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    con = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=con)

def show_new(request, news_id):
    #news = get_object_or_404(News, pk=news_id)
    news = News.objects.get(pk=news_id)
    return render(request, 'news/single_new.html', {"new" : news,})

def add_news(request):
    if request.method=='POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            News.objects.create(**form.cleaned_data)
    else: form = NewsForm()
    return render(request, 'news/add_news.html', {'form':form})