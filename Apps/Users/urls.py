from django.urls import path
from .views import registration_view, activate

from rest_framework.authtoken.views import obtain_auth_token

app_name = "Users"

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]