from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('assets', views.AssetViewSet)
app_name = 'coinapi'
urlpatterns = [
    path('price/<str:asset>', views.view_coin_price, name='price'),
    path('price/<str:asset>/<str:time>', views.view_coin_price, name='price'),
    path('', include(router.urls))
]
