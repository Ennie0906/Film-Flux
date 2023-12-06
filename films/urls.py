from django.urls import path
from .views import AddReview, FilmList, FilmDetail




urlpatterns = [
    path("", AddReview.as_view(), name="add_review"),
    path("films/", FilmList.as_view(), name="films"),
    path('<int:pk>/', FilmDetail.as_view(), name="film_detail")
]
