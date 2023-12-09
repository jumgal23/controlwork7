from django.urls import path
from book.views import index_view

urlpatterns = [
    path('', index_view, name='index'),
]