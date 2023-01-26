from django.urls import path
from .views import (
    FilmListView,
    FilmCreateView,
    FilmDetailView,
    FilmUpdateView,
    FilmDeleteView,
    GenreCreateView,
    GenreDetailView,
    GenreUpdateView,
    GenreListView,
    GenreDeleteView,
)

urlpatterns = [
    path("films", FilmListView.as_view(), name="film_all"),
    path("films/<int:pk>/detail", FilmDetailView.as_view(), name="film_detail"),
    path("films/create/", FilmCreateView.as_view(), name="film_create"),
    path("films/<int:pk>/update/", FilmUpdateView.as_view(), name="film_update"),
    path("films/<int:pk>/delete/", FilmDeleteView.as_view(), name="film_delete"),
    path("genres", GenreListView.as_view(), name="genre_all"),
    path("genres/<int:pk>/detail", GenreDetailView.as_view(), name="genre_detail"),
    path("genres/create/", GenreCreateView.as_view(), name="genre_create"),
    path("genres/<int:pk>/update/", GenreUpdateView.as_view(), name="genre_update"),
    path("genres/<int:pk>/delete/", GenreDeleteView.as_view(), name="genre_delete"),
]
