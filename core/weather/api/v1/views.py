from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.views import APIView
import requests


openweather_api = (
    "https://api.openweathermap.org"
    "/data/2.5/weather?lat=44.34&lon=10.99&appid="
    "5380fcd9a358195c8a78422756e9ef65"
)


class WeatherApiView(APIView):
    @method_decorator(cache_page(60 * 20))
    def get(self, request, format=None):
        content = {"weather_data": requests.get(openweather_api).json()}
        weather_description = content["weather_data"]["weather"][0]["description"]
        return Response(weather_description)
