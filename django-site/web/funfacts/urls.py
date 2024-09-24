# funfacts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.funfacts_list, name='funfacts_list'),
    path('create/', views.create_funfact, name='create_funfact'),
    path('vote/<int:funfact_id>/<str:vote_value>/', views.vote_funfact, name='vote_funfact'),
]
