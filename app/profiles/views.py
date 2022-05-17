from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import PhotoSerializer, ProfileSerializer
from .models import Photo, Profile


class UserProfile(APIView):

    def post(self, request, format=None):
        '''
        Method creates a profile

        - Token Required
        '''
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''
        Method returns a profile by PK

        - Token Required
        '''
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
