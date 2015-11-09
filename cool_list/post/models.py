from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "title: {}, date_added: {}, date_modified: {}".format(self.title,
                                                                     self.date_added,
                                                                     self.date_modified)


class SubCategory(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "title: {}, category: {}".format(self.title, self.category,)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user_email = models.EmailField(max_length=200)
    phone_number = models.IntegerField()
    zipcode = models.CharField(max_length=10)
    images = models.ImageField()
    sub_category = models.ForeignKey(SubCategory)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "title: {}, Description: {}, price: {}, user_email: {}, phone_number: {}, zipcode: {}," \
                " images: {}, date_added: {}, date_modified: {}".format(self.title,
                                                                        self.description,
                                                                        self.price,
                                                                        self.user_email,
                                                                        self.phone_number,
                                                                        self.zipcode,
                                                                        self.images,
                                                                        self.date_added,
                                                                        self.date_modified)


class Location(models.Model):
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return "state: {}, city: {}".format(self.state, self.city)
