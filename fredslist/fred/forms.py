from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class meta:
        model = Post
        fields = ('title', 'subcategory', 'user', 'description', 'images', 'location', 'created', 'modified')


class Category(forms.ModelForm):
    class meta:
        model = Category
        fields = 'title'


class SubCategory(forms.ModelForm):
    class meta:
        model = SubCategory
        fields = ('category', 'title')


class Location(forms.ModelForm):
    class meta:
        model = Location
        fields = ('state', 'city')






