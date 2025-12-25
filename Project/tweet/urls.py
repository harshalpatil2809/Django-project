from django.urls import path
from . import views


urlpatterns = [
    path('', views.tweet, name='tweet'),
    path('showtweet/', views.Showtweet, name='showtweet'),
    path('create/', views.CreateTweet, name='Create_T'),
    path('<int:tweet_id>/edit/', views.EditTweet, name='Edit_T'),
    path('<int:tweet_id>/delete/', views.DeleteTweet, name='Delete_T'),
    path('<int:tweet_id>/fulltweet/', views.FullTweet, name='Full_T'),
    path('register/', views.UserRegistration, name='register'),
    path('login/', views.Login, name='login'),
] 