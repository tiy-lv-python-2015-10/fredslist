from django.contrib import admin
from posting.models import Category, SubCategory, Post, City, State


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'title')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('location', 'subcategory', 'title', 'description', 'user', 'phone', 'price')


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
