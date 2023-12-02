from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = 'home/index.html'


# def home(request):
#     return render(request, 'film-flux/base.html')

# def movie_detail(request, movie_id):
#     return render(request, 'film_blog/movie_detail.html', {'movie_id': movie_id})