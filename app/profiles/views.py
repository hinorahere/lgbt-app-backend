from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import PhotoSerializer, ProfileSerializer
from .models import Photo, Profile

class UserProfile(APIView):

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)