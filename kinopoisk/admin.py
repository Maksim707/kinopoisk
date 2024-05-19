from django.contrib import admin
from .models import *


@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "role",
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "rating",
        "poster",
    )


@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = (
        "movie",
        "author",
        "text",
    )
