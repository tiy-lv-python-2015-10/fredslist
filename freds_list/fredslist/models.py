from django.db import models
from django.contrib.auth.models import User

class State(models.Model):
    state = models.CharField(max_length=21)

    def __str__(self):
        return '{}'.format(self.state)

class City(models.Model):
    state = models.ForeignKey(State)
    city = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.city)

class Category(models.Model):
    city = models.ForeignKey(City)
    title = models.CharField(max_length=255)

    def __str__(self):
        return "Location: {}, Category: {}".format(self.city, self.title)


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=255)

    def __str__(self):
        return "Category: {}, {}".format(self.category, self.title)


class Post(models.Model):
    sub_category = models.ForeignKey(SubCategory)
    location = models.OneToOneField(City)
    user = models.OneToOneField(User)

    phone_number = models.CharField(max_length=15)  # needs validator
    contact_name = models.CharField(max_length=255)
    posting_title = models.CharField(max_length=255)
    price = models.CharField(max_length=10, null=True, blank=True)  # needs validator
    specific_location = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255)  # needs validator
    posting_body = models.TextField()


    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def post_images(self):
        return self.images_set.all()

    def __str__(self):
        return "{}, {}".format(self.sub_category, self.posting_title)


class Images(models.Model):
    post = models.ForeignKey(Post)
    image = models.ImageField(upload_to='fredslist_images', blank=True, null=True)

    def __str__(self):
        return "{}, {}".format(self.post, self.image)
