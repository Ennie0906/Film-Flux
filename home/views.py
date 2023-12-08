from django.shortcuts import render
from django.views.generic import TemplateView
from films.models import Films

class Index(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        films = Films.objects.all()  # Adjust this query based on your model
        context['films'] = films
        return context



# def home(request):
#     return render(request, 'film-flux/base.html')

# def movie_detail(request, movie_id):
#     return render(request, 'film_blog/movie_detail.html', {'movie_id': movie_id})