
from django.urls import path
from .views import AddReview
from .views import Films


urlpatterns = [
    path('', AddReview.as_view(), name='add_review'),
    path('films/', Films.as_view(), name = 'films'),
]
