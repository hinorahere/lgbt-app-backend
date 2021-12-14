from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings

from accounts.models import CustomUser as User

# {"id":5}
@api_view(['GET','POST'])
def match(request):
    if request.method == 'POST':
        # current_user = request.user.id
        # prospective_user = request.data["id"]
        # User = settings.AUTH_USER_MODEL
        try:
            current_user = User.objects.get(id=request.user.id)
        except Exception as e:
            raise
        print(dir(current_user))
        print(current_user.pk)
        print(current_user.prospects)
        print("^^^^^^^^^^^^^^^^")
        return Response("current_user")
    return Response({"message": "GET"})

class MatchList(APIView):

    def get(self, request, format=None):
        return Response("MatchList GET")

    def post(self, request, format=None):
        return Response("MatchList POST")

class MatchDetail(APIView):

    def get(self, request, pk, format=None):
        return Response("MatchDetail GET")

    def put(self, request, pk, format=None):
        return Response("MatchDetail PUT")

    def patch(self, request, pk, format=None):
        return Response("MatchDetail PATCH")

    def delete(self, request, pk, format=None):
        return Response("MatchDetail DELETE")
