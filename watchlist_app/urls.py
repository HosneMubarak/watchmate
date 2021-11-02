from django.urls import path
# from .views import movie_list, movie_details
from .views import WatchListListAV,WatchListDetailsAV, StreamPlatformListAV, StreamPlatformDetailsAV

urlpatterns = [
    # path('list', movie_list, name='movie-list'),
    # path('movie/<int:pk>', movie_details, name='movie_detailss'),

    path('movie_list', WatchListListAV.as_view(), name='movie-list'),
    path('movie/<int:pk>', WatchListDetailsAV.as_view(), name='movie_details'),

    path('platform_list', StreamPlatformListAV.as_view(), name='platform_list'),
    path('platform/<int:pk>', StreamPlatformDetailsAV.as_view(), name='platform-details'),
]