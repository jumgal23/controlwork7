from django.contrib import admin
from book.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'name', 'email', 'text', 'created_at', 'updated_at']
    list_display_links = ['id', 'status', 'name', 'email']
    list_filter = ['status', 'name']
    search_fields = ['id', 'status', 'name']
    fields = ['status', 'name', 'email', 'text']
    readonly_fields = ['created_at', 'updated_at']
