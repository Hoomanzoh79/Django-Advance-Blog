from django.urls import path
from . import views


urlpatterns = [
    path('registration/',views.RegistrationApiView.as_view(),name='registration'),
    path('token/login/',views.CustomAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustomDiscardAuthToken.as_view(),name='token-logout'),
]