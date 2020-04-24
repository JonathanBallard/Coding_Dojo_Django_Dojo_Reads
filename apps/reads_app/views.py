from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
import datetime
 
 
# Create your views here. 
def index(request): 
    thisUser = User.objects.get(id=request.session['cur_user'])

    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now()

    recentReviewsAll = Review.objects.order_by('-created_at')
    firstThreeRecentReviews = []

    if len(recentReviewsAll) > 2:
        firstThreeRecentReviews.append(recentReviewsAll[0])
        firstThreeRecentReviews.append(recentReviewsAll[1])
        firstThreeRecentReviews.append(recentReviewsAll[2])
    else:
        firstThreeRecentReviews = []

    allReviews = Review.objects.all()

    context = {
        "recent_reviews" : firstThreeRecentReviews,
        "all_reviews" : allReviews,
        "thisUser" : thisUser,

    }

    return render(request, 'reads_app/index.html', context) 



def thisBook(request, id): 
    thisUser = User.objects.get(id=request.session['cur_user'])
    thisBook = Book.objects.get(id=id)

    context = {
        "thisUser" : thisUser,
        "thisBook" : thisBook,

    }


    return render(request, 'reads_app/thisBook.html', context)

def createReview(request): 
    thisUser = User.objects.get(id=request.session['cur_user'])
    thisBook = Book.objects.get(id=request.POST['bookId'])

    errors = Review.objects.review_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
    else:
        newReview = Review.objects.new_review(request.POST,thisUser,thisBook)

    return redirect('/books/' + str(thisBook.id))
    



def deleteReview(request, id): 
    thisUser = User.objects.get(id=request.session['cur_user'])
    delReview = Review.objects.get(id=id)

    if delReview.reviewer.id == thisUser.id:
        delReview.delete()
    else:
        return redirect('/books/')

    return redirect('/books/')


def newBook(request): 
    thisUser = User.objects.get(id=request.session['cur_user'])

    if len(request.POST['author_typed']):
        thisAuthor = Author.objects.new_author(request.POST)
        chosenAuthor = thisAuthor
    else:
        authorId = request.POST['author_select']
        chosenAuthor = Author.objects.get(id=authorId)

    

    
    errors = Book.objects.book_validator(request.POST)
    review_errors = Review.objects.review_validator(request.POST)

    if len(review_errors) > 0:
        for k,v in review_errors.items():
            messages.error(request, v)
    else:
        if len(errors) > 0:
            for k,v in errors.items():
                messages.error(request, v)
        else:
            newBook = Book.objects.new_book(request.POST, chosenAuthor)
            newReview = Review.objects.new_review(request.POST,thisUser,newBook)
            return redirect('/books/')

    return redirect('/books/add/')




def thisUser(request, id): 
    thisUser = User.objects.get(id=request.session['cur_user'])
    chosenUser = User.objects.get(id=id)

    # Might be a problem with the annotation in thisUser.html
    totalReviews = User.objects.annotate(totalReviews = Count('reviews_written'))
    context = {
        "thisUser" : thisUser,
        "chosenUser" : chosenUser,
        "total_reviews" : chosenUser.totalReviews,


    }
    return render(request, 'reads_app/thisUser.html', context)




def addBook(request): 
    thisUser = User.objects.get(id=request.session['cur_user'])

    allAuthors = Author.objects.all()
    context = {
        "all_authors" : allAuthors,
        "thisUser" : thisUser,

    }

    return render(request,'reads_app/addBook.html',context)






def destroy(request):
    request.session.flush() 
    return redirect('/')



















