from django.urls import path
from . import views


urlpatterns = [
    path('', views.tweet, name='tweet'),
    path('showtweet/', views.Showtweet, name='showtweet'),
    path('create/', views.CreateTweet, name='Create_T')
] 