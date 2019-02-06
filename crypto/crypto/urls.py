from django.contrib import admin, auth
from django.urls import path, include
from rest_framework.authtoken import views as authviews
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Crypto API')

urlpatterns = [
    # Documentation
    path('doc/', schema_view, name='doc'),
    # Prime URLS
    path('', include('prime.urls', namespace='prime')),
    # CoinAPI URLS
    path('coin/', include('coinapi.urls', namespace='coinapi')),
    # Default admin panel
    path('admin/', admin.site.urls),
    # REST Endpoint for API Token
    path('login/', authviews.obtain_auth_token, name='login'),
    # Default registration endpoints
    path('accounts/', include('django.contrib.auth.urls'))

]
