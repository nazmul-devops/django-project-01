from django.contrib import admin

from dbpost.models.models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'user', 'published', 'updated']
    list_filter = ['user__username']
    search_fields = ['title', 'description', 'user']

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']



