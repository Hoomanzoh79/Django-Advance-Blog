from django.urls import path
from ..views import ProfileApiView


urlpatterns = [
    # profile
    path("", ProfileApiView.as_view(), name="profile"),
]
