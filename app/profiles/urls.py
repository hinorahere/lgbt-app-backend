from django.urls import path, include

from rest_framework import routers

from .views import PhotoViewSet, ProfileViewSet


router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'photo', PhotoViewSet, basename='photo')


urlpatterns = [
    path('', include(router.urls)),
]
