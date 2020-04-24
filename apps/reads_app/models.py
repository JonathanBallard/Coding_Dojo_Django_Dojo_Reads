from django.db import models 
import re 
from apps.login_reg.models import *
 
# create your models here 
# Field Types Link: https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types 

class BookManager(models.Manager):
    pass

class ReviewManager(models.Manager):
    pass


class AuthorManager(models.Manager):
    pass


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField('Author', related_name="books_written", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    content = models.TextField()
    subject_of_review = models.ForeignKey('Book', related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)














