# from django.db import models
# from django.contrib.auth.models import User
#
#
# class Location(models.Model):
#     state = models.CharField(max_length=21)
#     city = models.CharField(max_length=255)
#     zip_code = models.CharField(max_length=10)
#
#
# class Category(models.Model):
#     location = models.ForeignKey(Location)
#     title = models.CharField(max_length=255)
#
#
# class SubCategory(models.Model):
#     category = models.ForeignKey(Category)
#     title = models.CharField(max_length=255)
#
#
# class Post(models.Model):
#     sub_category = models.ForeignKey(SubCategory)
#     location = models.OneToOneField(Location)
#     user = models.OneToOneField(User)
#
#     phone_number = models.CharField(max_length=15)  # needs validator
#     contact_name = models.CharField(max_length=255)
#     posting_title = models.CharField(max_length=255)
#     price = models.CharField(max_length=10, null=True, blank=True)  # needs validator
#     specific_location = models.CharField(max_length=255, null=True, blank=True)
#     postal_code = models.CharField(max_length=255)  # needs validator
#     posting_body = models.TextField()
#
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#
#
# class Images(models.Model):
#     post = models.ForeignKey(Post)
#     image = models.ImageField(upload_to='fredslist_images', blank=True, null=True)
