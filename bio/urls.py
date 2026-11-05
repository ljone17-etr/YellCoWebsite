# opens a connection/path for new app bio

from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="bio")
]
