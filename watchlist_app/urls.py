from django.urls import path
from .views import movie_list, movie_details


urlpatterns = [
    path('list', movie_list, name='movie-list'),
    path('movie/<int:pk>', movie_details, name='movie_detailss'),
]