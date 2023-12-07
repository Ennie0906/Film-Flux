from django.views.generic import (CreateView, ListView, DetailView ,DeleteView, UpdateView)

from django.contrib.auth.mixins import (UserPassesTestMixin, LoginRequiredMixin)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Films
from .forms import FilmForm
from django.urls import reverse_lazy


class FilmList(ListView):
    """
    View all films
    """

    template_name = "films/films.html"
    model = Films
    context_object_name = "films"


class FilmDetail(DetailView):
    """View a single film"""

    template_name = "films/film_detail.html"
    model = Films
    context_object_name = "film"


class AddReview(LoginRequiredMixin, CreateView):
    """Add Review"""

    template_name = "films/add_review.html"
    model = Films
    form_class = FilmForm
    success_url = "/films/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)


class EditFilm(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a film"""
    template_name = 'films/edit_film.html'
    model = Films
    form_class = FilmForm

    def get_success_url(self):
        return reverse_lazy('films') 

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteFilm(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a film """
    model = Films
    success_url = '/films/'
    template_name = 'films/film_confirm_delete.html'

    def test_func(self):
        return self.request.user == self.get_object().user