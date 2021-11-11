from django.shortcuts import render
from .models import MovieList, StreamPlatform, Review
from .serializers import MovieListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class ReviewCreate(CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movielist = MovieList.objects.get(pk=pk)
        serializer.save(movielist=movielist)


class ReviewList(ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(movielist=pk)


class ReviewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class StreamPlatformListVS(viewsets.ModelViewSet):
    serializer_class = StreamPlatformSerializer
    queryset = StreamPlatform.objects.all()



# class StreamPlatformListAV(APIView):
#     def get(self, request):
#         platform = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(platform, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieListListAV(APIView):
    def get(self, request):
        movies = MovieList.objects.all()
        serializer = MovieListSerializer(movies, many=True, )
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailsAV(APIView):
    def get(self, request, pk=None):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'errors': 'platform not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk=None):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer \
            (platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk=None):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


class MovieListDetailsAV(APIView):
    def get(self, request, pk=None):
        try:
            movie = MovieList.objects.get(pk=pk)
        except MovieList.DoesNotExist:
            return Response({'errors': 'movie not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk=None):
        movie = MovieList.objects.get(pk=pk)
        serializer = MovieListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk=None):
        movie = MovieList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         serializer = MovieSerializer(movie, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return serializer.errors
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movie_detail = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'movie dose not exist'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie_detail)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
