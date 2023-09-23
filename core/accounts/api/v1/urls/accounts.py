from django.urls import path
from .. import views
from rest_framework_simplejwt.views import (TokenRefreshView,TokenVerifyView)


urlpatterns = [
    # registration
    path('registration/',views.RegistrationApiView.as_view(),name='registration'),

    # activation
    path('activation/confirm/<str:token>/',views.ActivationApiView.as_view(),name='activation'),
    # activation resend
    path('activation/resend/',views.ActivationResendApiView.as_view(),name='activation-resend'),
    #token login and logout
    path('token/login/',views.CustomAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustomDiscardAuthToken.as_view(),name='token-logout'),

    #jwt token login
    path('jwt/create/',views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

    # change password
    path('change-password/',views.ChangePasswordApiView.as_view(),name='change-password'),

    # reset password link via email
    path('reset-password/',views.ResetPasswordEmailApiView.as_view(),name='reset-password'),

    # reset password confirm
    path('reset-password/confirm/<str:token>/',views.ResetPasswordConfirmApiView.as_view(),name='reset-password-confirm'),

    # confirmation
    path('test-email/',views.TestEmailSend.as_view(),name='test-email'),

]