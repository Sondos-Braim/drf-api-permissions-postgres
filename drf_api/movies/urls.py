from django.contrib import admin
from django.urls import path, include


from .views import MovieDetailsView, MoviesListView


urlpatterns = [
    path('', MoviesListView.as_view(), name='movies'),
    path('<int:pk>/', MovieDetailsView.as_view(), name='movie_details'),
]