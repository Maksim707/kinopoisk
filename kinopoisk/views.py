from django.shortcuts import render
from .models import *


def movies(request):
    movie = Movie.objects.all()
    return render(request, "kinopoisk/movies.html")


def actors(request):
    actor = MoviePerson.objects.filter(role=MoviePerson.RoleType.ACTOR)
    return render(request, "kinopoisk/actors.html")


def directors(request):
    director = MoviePerson.objects.filter(role=MoviePerson.RoleType.DIRECTOR)
    return render(request, "kinopoisk/directors.html")


def genres(request):
    genre = Genre.objects.filter(name="")
    return render(request, "kinopoisk/genres.html")


def movie_detail(request):
    movie_detail = Movie.objects.all()
    return render(request, "kinopoisk/movie_detail.html")


def actor_detail(request):
    actor_detail = MoviePerson.objects.all()
    return render(request, "kinopoisk/actor_detail.html")


def director_detail(request):
    director_detail = MoviePerson.objects.all()
    return render(request, "kinopoisk/director_detail.html")


def genre_detail(request):
    genre_detail = Genre.objects.all()
    return render(request, "kinopoisk/genre_detail.html")
