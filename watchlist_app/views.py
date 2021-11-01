from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse


def movie_list(request):
    movie = Movie.objects.all()
    data = {
        'movies': list(movie.values())
    }
    return JsonResponse(data)


def movie_details(request, pk):
    movie_detail = Movie.objects.get(pk=pk)
    data = {
        'name': movie_detail.name,
        'description': movie_detail.description,
        'active': movie_detail.active,
    }
    return JsonResponse(data)
