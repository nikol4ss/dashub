from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.home, name="Dashboard"),
]
