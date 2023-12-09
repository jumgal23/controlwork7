from django.shortcuts import render, get_object_or_404, redirect
from book.models import Article
from book.forms import ArticleForm
from django.utils import timezone


def index_view(request):
    articles = Article.objects.filter(status="active").order_by('-created_at')
    return render(request, 'index.html', {'articles': articles})


def article_create_view(request):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, 'article_create.html', {'form': form})
    elif request.method == "POST":
        form = ArticleForm(data=request.POST)

        if form.is_valid():
            article = Article.objects.create(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                text=form.cleaned_data.get('text')
            )
            return redirect('index')
        else:
            return render(request, 'article_create.html', {'form': form})


def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        form = ArticleForm(initial={
            'name': article.name,
            'email': article.email,
            'text': article.text
        })
        return render(request, 'article_update.html', {'form': form})
    elif request.method == "POST":

        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.name = form.cleaned_data.get('name')
            article.email = form.cleaned_data.get('email')
            article.text = form.cleaned_data.get('text')
            article.updated_at = timezone.now()
            article.save()
            return redirect('index',)
        else:
            return render(request, 'article_update.html', {'form': form})


def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, 'article_delete.html', {'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')
