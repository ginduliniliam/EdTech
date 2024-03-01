from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Author(models.Model):
    # model Author
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)  # foreign key for user model
    biography = models.TextField()  # biography author

    def __str__(self):
        return self.user.username


class Product(models.Model):
    # model Product
    title = models.CharField(max_length=250)  # Product title
    slug = models.SlugField(max_length=250, default='')  # Product slug
    description = models.TextField(default='')  # Product description
    start_sales = models.DateTimeField()  # start of product sales  (start working/studying)
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Product price
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE)  # Product author

    def __str__(self):
        return self.title

    def available(self):
        # checks whether the product is currently available
        return timezone.now() >= self.start_sales


class Lesson(models.Model):
    # model lesson
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)  # foreign key for product model
    title = models.CharField(max_length=100)  # Lesson title
    video_link = models.URLField()  # Video link in Lesson


class Membership(models.Model):
    # model Membership
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)  # foreign key for user model
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)  # foreign key for product model
    access_granted = models.BooleanField(default=False)  # indicates whether the user has access to the product

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
