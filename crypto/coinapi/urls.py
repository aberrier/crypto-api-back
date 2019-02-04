from django.urls import path

from . import views

urlpatterns = [
    path('price/<str:asset>', views.view_coin_price, name='price'),
    path('price/<str:asset>/<str:time>', views.view_coin_price, name='price')
]