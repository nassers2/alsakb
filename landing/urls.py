from django.urls import path

from . import views

app_name = "landing"

urlpatterns = [
    path("", views.index, name="index"),
    path("thank-you/", views.thank_you, name="thank_you"),
]
