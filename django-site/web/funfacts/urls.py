# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_games_list, name='video_games_list'),
    path('create/', views.create_video_game, name='create_video_game'),
    path('vote/<int:video_game_id>/<int:vote_value>/', views.vote_video_game, name='vote_video_game'),
]