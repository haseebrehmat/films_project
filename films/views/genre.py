from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ..models import Genre
from ..forms import GenreForm


class GenreBaseView(View):
    model = Genre
    success_url = reverse_lazy("genre_all")

    def get_queryset(self):
        return super().get_queryset().prefetch_related("film_set").all()


class GenreListView(GenreBaseView, ListView):

    """View to list all genres.
    Use the 'genre_list' variable in the template
    to access all Genre objects"""


class GenreDetailView(GenreBaseView, DetailView):
    """View to list the details from one genre.
    Use the 'genre' variable in the template to access
    the specific genre here and in the Views below"""


class GenreCreateView(GenreBaseView, CreateView):
    """View to create a new genre"""

    form_class = GenreForm


class GenreUpdateView(GenreBaseView, UpdateView):
    """View to update a genre"""

    form_class = GenreForm


class GenreDeleteView(GenreBaseView, DeleteView):
    """View to delete a genre"""
