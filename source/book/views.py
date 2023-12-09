from django.shortcuts import render, get_object_or_404, redirect
from book.models import Article


def index_view(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

