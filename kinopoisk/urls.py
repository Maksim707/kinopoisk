from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', movies ,name='movies'),
    path('actors/', actors ,name='actors'),
    path('directors/', directors ,name='directors'),
    path('genres/', genres ,name='genres'),
    path('movie/<int:id>/', movie_detail , name='movie_detail'),
    path('actor/<int:id>/',actor_detail, name='actor_detail'),
    path('director/<int:id>/', director_detail , name='director_detail'),
    path('genre/<int:id>/', genre_detail ,name='genre_detail'),
    ]