# api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('facts/', views.funfacts_all, name='funfacts_all'),
    path('votes/', views.votes_all, name='votes_all'),
]
