from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

urlpatterns = [
    path('register/', views.RegisterUserAPIView.as_view(), name='register_user'),
    path('login_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login_token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login_token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]