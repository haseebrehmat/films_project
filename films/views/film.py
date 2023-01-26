from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ..models import Film
from ..forms import FilmForm


class FilmBaseView(View):
    model = Film
    success_url = reverse_lazy("film_all")


class FilmListView(FilmBaseView, ListView):
    """View to list all films.
    Use the 'film_list' variable in the template
    to access all Film objects"""


class FilmDetailView(FilmBaseView, DetailView):
    """View to list the details from one film.
    Use the 'film' variable in the template to access
    the specific film here and in the Views below"""


class FilmCreateView(FilmBaseView, CreateView):
    """View to create a new film"""

    form_class = FilmForm


class FilmUpdateView(FilmBaseView, UpdateView):
    """View to update a film"""

    form_class = FilmForm


class FilmDeleteView(FilmBaseView, DeleteView):
    """View to delete a film"""
