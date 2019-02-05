from django.urls import path, include
from rest_framework import routers

from . import views
from . import viewsets

router = routers.DefaultRouter()
router.register('users', viewsets.UserViewSet)
router.register('alerts', viewsets.AlertViewSet, basename='alert')

alert_retrieve = viewsets.AlertViewSet.as_view({
    'get': 'retrieve'
})
app_name = 'prime'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('create/alert/', views.AlertCreate.as_view(), name='alerts_create'),
    path('update/alert/<int:pk>/', views.AlertUpdate.as_view(), name='alerts_update'),
    path('delete/alert/<int:pk>/', views.AlertDelete.as_view(), name='alerts_delete'),
    path('', include((router.urls, 'alerts'), namespace='alerts'))
]
