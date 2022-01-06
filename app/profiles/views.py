from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

from .serializers import PhotoSerializer, ProfileSerializer
from .models import Photo, Profile


class PhotoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = Photo.objects.all().order_by('id')
    serializer_class = PhotoSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
