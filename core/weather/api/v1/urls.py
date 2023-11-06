from django.urls import path, include
from .views import WeatherApiView

app_name = "api-v1"

urlpatterns = [
    path("",WeatherApiView.as_view(),name="weather"),
]
