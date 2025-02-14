from django.contrib import admin
from .models import Post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'category')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('title', 'content_small', 'content_full', 'keywords')
    prepopulated_fields = {'keywords': ('title',)}

