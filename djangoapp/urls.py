from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("name/<str:name>", views.findByName)
]