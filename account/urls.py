from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('register/', views.EmployeeRegisterAPIView.as_view(), name="Register Author"),
    path('', include('rest_framework.urls')),
    path('token/', obtain_auth_token),
]

