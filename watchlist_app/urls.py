from django.urls import path, include
# from .views import movie_list, movie_details
from .views import StreamPlatformListVS, ReviewDetail,ReviewCreate, WatchListListAV,WatchListDetailsAV, StreamPlatformDetailsAV, ReviewList
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('stream', StreamPlatformListVS, basename='streamPlatform')


urlpatterns = [
    # path('list', movie_list, name='movie-list'),
    # path('movie/<int:pk>', movie_details, name='movie_detailss'),

    path('list', WatchListListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailsAV.as_view(), name='movie_details'),
    path('', include(router.urls)),
    # path('streem', StreamPlatformListAV.as_view(), name='platform_list'),
    # path('streem/<int:pk>', StreamPlatformDetailsAV.as_view(), name='streamplatform-detail'),

    # path('review', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-details')
    path('streem/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('streem/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('streem/review/<int:pk>', ReviewDetail.as_view(), name='review-details')
]