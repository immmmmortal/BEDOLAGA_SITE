import datetime

from django.db import models
from django.urls import reverse_lazy


class Ad(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    price = models.FloatField()
    item_description = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Review(models.Model):
    reviewed_ad = models.ForeignKey('Ad', on_delete=models.CASCADE, blank=True, null=True)
    review_text = models.TextField()
    review_rating = models.IntegerField()
    review_author = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.review_author.name


class User(models.Model):
    name = models.TextField()
    email = models.EmailField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
