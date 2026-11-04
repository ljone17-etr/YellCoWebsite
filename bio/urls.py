# opens a connection/path for new app bio

from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomepageView.as_view(), name='bio'),
]
