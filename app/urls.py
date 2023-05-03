from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'client', views.ClientViewSet, basename='clients')
router.register(r'project', views.ProjectViewSet, basename='projects')

urlpatterns = [
    path('', include(router.urls)),
]
