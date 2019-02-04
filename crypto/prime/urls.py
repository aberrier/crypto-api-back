from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('alerts', views.AlertViewSet, basename='get_queryset')


urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
]