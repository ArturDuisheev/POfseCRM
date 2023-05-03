from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
<<<<<<< HEAD
router.register(r'client', views.ClientViewSet)
router.register(r'project', views.ProjectViewSet)
=======
# router.register(r'register', )
router.register(r'client', views.ClientViewSet, basename='clients')
router.register(r'project', views.ProjectViewSet, basename='projects')
>>>>>>> 6b20bd34a3023f492a43ca8125e1bf0baacaa042

urlpatterns = [
    path('', include(router.urls)),
]
