from django.urls import path, include
from rest_framework import routers
from django.views.generic.base import TemplateView
from . import viewsets
from . import views

router = routers.DefaultRouter()
router.register('users', viewsets.UserViewSet)
router.register('alerts', viewsets.AlertViewSet, basename='alert')

alert_retrieve = viewsets.AlertViewSet.as_view({
    'get': 'retrieve'
})
app_name = 'prime'

urlpatterns = [
    path('', TemplateView.as_view(template_name='prime/index.html'), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('test/', views.AlertDetail.as_view()),
    path('test/<int:pk>/', views.AlertDetail.as_view()),
    path('', include((router.urls, 'alerts'), namespace='alerts'))
]
