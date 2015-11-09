from django import forms
from django.forms import Textarea, BaseInlineFormSet
from posting.models import Post


class PostForm():
    class Meta:
        model = Post
        fields = ('title', 'description', 'phone', 'price', 'subcategory', )
        widgets = {
            'description': Textarea(attrs={'rows': 2})
        }