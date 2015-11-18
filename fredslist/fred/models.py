from django.db import models
from users.models import Profile


class Category(models.Model):
    title = models.CharField(max_length=50)


class SubCategory(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=150)


class Post(models.Model):
    title = models.CharField(max_length=150)
    sub_category = models.ForeignKey(SubCategory)
    description = models.TextField()
    images = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Location(models.Model):
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
