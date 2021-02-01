from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slog','jpublished','status')
    list_filter = ('published','status')
    search_fields = ('title','description')
    prepopulated_fields = {'slog':('title',)}
    ordering = ['status','published']


admin.site.register(Article, ArticleAdmin)
