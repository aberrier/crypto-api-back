from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('alerts', views.AlertViewSet, basename='alert')

alert_retrieve = views.AlertViewSet.as_view({
    'get': 'retrieve'
})
app_name = 'prime'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.AlertDetail.as_view()),
    path('test/<int:pk>/', views.AlertDetail.as_view()),
    # path('wow/<int:pk>', alert_retrieve, name='alerts'),
    path('', include((router.urls, 'alerts'), namespace='alerts'))
]