# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('videogames/', views.video_games_all, name='video_games_all'),
    path('votes/', views.votes_all, name='votes_all'),
]