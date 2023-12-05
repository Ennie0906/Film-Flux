from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Films
from .forms import FilmForm

class AddReview(LoginRequiredMixin, CreateView):
    """ Add Review """
    template_name = 'films/add_review.html'
    model = Films
    form_class = FilmForm
    success_url = '/films/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)

    