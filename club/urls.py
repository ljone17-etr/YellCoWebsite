# This is the html webpage that shows the club's home page.
# It shows upcoming meetings and club values. 
# It also has links to the finance page and the old business page. 

from django.urls import path

from . import views

app_name = "club"

urlpatterns = [
    path("", views.home, name="home"),
    path("finance/", views.finance, name="finance"),
    path("old-business/", views.old_business, name="old_business"),
]

