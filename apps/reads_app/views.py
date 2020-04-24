from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
 
 
 
# Create your views here. 
def index(request): 
    return render(request, 'reads_app/index.html') 
