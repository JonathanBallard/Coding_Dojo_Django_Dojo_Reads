from django.urls import path 
from django.conf.urls import url 
from . import views 

urlpatterns = [ 
    path('', views.index), 
    path('<int:id>/', views.thisBook), 
    path('user/<int:id>/', views.thisUser), 
    path('add/', views.addBook), 
    path('review/', views.createReview), 
    path('newBook/', views.newBook), 
    path('review/delete/<int:id>', views.deleteReview), 
    path('destroy/', views.destroy), 

] 
