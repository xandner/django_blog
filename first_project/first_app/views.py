from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article


# Create your views here.

def home(request):
    context = {
        'articles': Article.objects.filter(status='p').order_by('published')
    }
    return render(request, "blog/home.html", context=context)


def detail(request, slug):
    context = {
        'article': Article.objects.get(slog=slug)
    }
    return render(request, "blog/detail.html", context=context)