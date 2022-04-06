from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("schemes", views.schemes, name="schemes"),
    path("prices", views.prices, name="prices"),
    path("result", views.result, name = "result"),
    path("load", views.load, name = "load"),
    path("temp", views.temp, name="temp")
]