from django.contrib import admin
from peteslist.models import Location, Type, Category, Post, Image


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'city')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'category', 'title', 'description', 'location', 'phone_number',
                    'contact_name', 'price', 'specific_location',
                    'manufacturer', 'model_name', 'serial_num', 'dimensions')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')