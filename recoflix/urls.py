from django.urls import path

from recoflix import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^movie/(?P<movie_id>\d+)/$', views.detail, name='detail'),
    path(r'^genre/(?P<genre_id>[\w-]+)/$', views.genre, name='genre'),
    path(r'^search/$', views.search_for_movie, name='search_for_movie'),
]
