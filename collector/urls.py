from django.urls import path
from collector import views

urlpatterns = [
    path(r'^log/$', views.log, name='log'),
]


