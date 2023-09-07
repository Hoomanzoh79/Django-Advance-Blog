from django.urls import path
from .. import views
from rest_framework_simplejwt.views import (TokenRefreshView,TokenVerifyView)


urlpatterns = [
    # registration
    path('registration/',views.RegistrationApiView.as_view(),name='registration'),

    #token login and logout
    path('token/login/',views.CustomAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustomDiscardAuthToken.as_view(),name='token-logout'),

    #jwt token login
    path('jwt/create/',views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

    # change password
    path('change-password/',views.ChangePasswordApiView.as_view(),name='change-password'),

]