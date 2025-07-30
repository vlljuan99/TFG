from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register('projects', views.ProjectViewSet, basename='projects')

urlpatterns = [
    path('ping/', views.PingView.as_view(), name='ping'),
    path('openproject/', views.OpenProjectStatusView.as_view(), name='openproject'),
    path('sync/', views.SyncView.as_view(), name='sync'),
    path('token-auth/', obtain_auth_token, name='token_auth'),
    path('', include(router.urls)),
]
