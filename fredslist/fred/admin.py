from django.contrib import admin
from fred.models import Category, SubCategory, Post, Location


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'title')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_category', 'description', 'images', 'created', 'modified')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('state', 'city')





