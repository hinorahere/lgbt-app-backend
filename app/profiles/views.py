from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

from .serializers import ProfileSerializer
from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = Profile.objects.all().order_by('first_name')
    serializer_class = ProfileSerializer
