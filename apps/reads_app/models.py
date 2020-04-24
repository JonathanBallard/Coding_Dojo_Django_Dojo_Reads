from django.db import models 
import re 
from apps.login_reg.models import *
from django.db.models import Count
 
# create your models here 
# Field Types Link: https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types 

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = "Title must contain at least 3 characters"
        return errors

    def new_book(self, postData, author):
        thisBook = Book.objects.create(title=postData['title'])
        thisBook.author.add(author)
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

    def author_other_validator(self, postData):
        errors = {}
        if len(postData['author_typed']) < 3:
            errors['author_typed'] = "Author's Name must contain at least 3 characters"
        return errors

    

    def new_author(self, postData):
        errors = {}
        if len(postData['author_typed']):
            nameExists = Author.objects.filter(first_name=postData['author_typed'])
        else:
            nameExists = Author.objects.filter(first_name=postData['first_name'], last_name=postData['last_name'])
        if len(nameExists) > 0:
            # errors['name_exists'] = "That Author Already Exists"
            # return errors
            print('That Author already exists!')
            return nameExists[0]
        else:
            if len(postData['author_typed']):
                thisAuthor = Author.objects.create(first_name=postData['author_typed'])
            else:
                thisAuthor = Author.objects.create(first_name=postData['first_name'], last_name=postData['last_name'])
            return thisAuthor


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField('Author', related_name="books_written")
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
    reviewer = models.ForeignKey('login_reg.User', related_name="reviews_written", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()














