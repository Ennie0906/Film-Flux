from django.urls import path
from .views import (AddReview, FilmList, FilmDetail, DeleteFilm, EditFilm)




urlpatterns = [
    path("add/", AddReview.as_view(), name="add_review"),
    path("", FilmList.as_view(), name="films"),
    path('<int:pk>/', FilmDetail.as_view(), name="film_detail"),
    path('delete/<int:pk>/', DeleteFilm.as_view(), name="delete_film"),
    path('edit/<int:pk>/', EditFilm.as_view(), name="edit_film"),

]
