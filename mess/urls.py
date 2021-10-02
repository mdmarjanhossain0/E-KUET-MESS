from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home_view, mess_details_view, space_details_view

app_name = "mess"
urlpatterns = [
    path('', home_view, name='home'),
    path('<mess_name>/', mess_details_view, name="mess_details"),
    path('<mess_name>/<space_name>/', space_details_view, name="space_details")
]