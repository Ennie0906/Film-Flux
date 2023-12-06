from django.views.generic import CreateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Films
from .forms import FilmForm



class Films(ListView):
    """ 
    View all films
    """
    template_name = 'films/films.html'
    model = Films
    context_object_name = 'films'

class AddReview(LoginRequiredMixin, CreateView):
    """ Add Review """
    template_name = 'films/add_review.html'
    model = Films
    form_class = FilmForm
    success_url = '/films/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)

    