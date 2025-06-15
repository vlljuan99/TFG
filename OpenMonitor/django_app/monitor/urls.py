from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('ping/', views.PingView.as_view(), name='ping'),
    path('openproject/', views.OpenProjectStatusView.as_view(), name='openproject'),
    path('token-auth/', obtain_auth_token, name='token_auth'),
]
