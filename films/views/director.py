from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ..models import Director
from ..forms import DirectorForm


class DirectorBaseView(View):
    model = Director
    success_url = reverse_lazy("director_all")

    def get_queryset(self):
        return super().get_queryset().prefetch_related("film_set").all()


class DirectorListView(DirectorBaseView, ListView):

    """View to list all directors.
    Use the 'director_list' variable in the template
    to access all Director objects"""


class DirectorDetailView(DirectorBaseView, DetailView):
    """View to list the details from one director.
    Use the 'director' variable in the template to access
    the specific director here and in the Views below"""


class DirectorCreateView(DirectorBaseView, CreateView):
    """View to create a new director"""

    form_class = DirectorForm


class DirectorUpdateView(DirectorBaseView, UpdateView):
    """View to update a director"""

    form_class = DirectorForm


class DirectorDeleteView(DirectorBaseView, DeleteView):
    """View to delete a director"""
