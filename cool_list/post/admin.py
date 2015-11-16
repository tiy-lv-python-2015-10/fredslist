from django.contrib import admin
from post.models import Post, Category, SubCategory, Location


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'user_email', 'phone_number',
                    'zipcode', 'images', 'date_added', 'date_modified']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_added', 'date_modified']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['state', 'city']
