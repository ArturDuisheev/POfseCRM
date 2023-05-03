from django.urls import path
from .views import SendMessageAPIView

urlpatterns = [
    path('chat/<str:room_name>/', SendMessageAPIView.as_view()),
]