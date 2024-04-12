from django.urls import path

from . import views

urlpatterns = [
    path("", views.user),
    path("<str:id>", views.userDetail)
]