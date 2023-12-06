from django.views.generic import CreateView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Films
from .forms import FilmForm


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
