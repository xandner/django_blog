from django.contrib import admin

from .models import Article,Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
    # ordering = ['status','published']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slog','jpublished','status','category_to_str')
    list_filter = ('published','status')
    search_fields = ('title','description')
    prepopulated_fields = {'slog':('title',)}
    # ordering = ['status','published']
    def category_to_str(self,obj):
        return ', '.join([category.title for category in obj.category.all() ])
    category_to_str.short_description='دسته بندی ها'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)

