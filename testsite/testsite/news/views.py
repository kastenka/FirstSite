from django.shortcuts import render
from .models import News, Category
from django.shortcuts import get_object_or_404


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'List of news',
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, template_name='news/category.html', context=context)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, template_name='news/view_news.html', context={"news_item": news_item})
