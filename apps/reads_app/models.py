from django.db import models 
import re 
from apps.login_reg.models import *
 
# create your models here 
# Field Types Link: https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types 

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = "Title must contain at least 3 characters"
        return errors

    def new_book(self, postData, author):
        thisBook = Book.objects.create(title=postData['title'], author=author)
        return thisBook

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}
        if len(postData['content']) < 8:
            errors['content'] = "content must contain at least 8 characters"
        if len(postData['rating']) < 1:
            errors['rating'] = "rating must be entered 1 to 5"
        return errors

    def new_review(self, postData, reviewer, book_reviewed):
        thisReview = Review.objects.create(content=postData['content'], reviewer=reviewer, rating=postData['rating'], book_reviewed=book_reviewed)
        return thisReview


class AuthorManager(models.Manager):
    def author_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors['first_name'] = "First Name must contain at least 3 characters"
        if len(postData['last_name']) < 3:
            errors['last_name'] = "Last Name must contain at least 3 characters"
        return errors

    def new_author(self, postData):
        thisAuthor = Author.objects.create(first_name=postData['first_name'], last_name=postData['last_name'])
        return thisAuthor


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField('Author', related_name="books_written", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()


class Review(models.Model):
    content = models.TextField()
    book_reviewed = models.ForeignKey('Book', related_name="reviews_received", on_delete=models.CASCADE)
    rating = models.IntegerField()
    reviewer = models.ForeignKey('User', related_name="reviews_written", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()














