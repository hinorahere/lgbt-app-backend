from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.models import CustomUser as User


@api_view(['POST'])
def match(request):
    if request.method == 'POST':
        # Type check(s)
        if not isinstance(request.data["prospective_id"], int):
            raise TypeError("prospective_id must be of type int")

        # Get current and prospective users
        try:
            prospective_id = int(request.data["prospective_id"])
            prospective_user = User.objects.get(id=prospective_id)
            current_user_id = request.user.id
            current_user = User.objects.get(id=current_user_id)
        except Exception as error:
            raise Exception(repr(error))

        # Determine if users are a match
        match = False
        for user_id in prospective_user.prospects.all():
            if int(str(user_id)) == current_user_id:
                match = True
                break

        # If match, update match fields on both users
        # else add prospective user to current_users prospective list
        if match:
            current_user.matches.add(prospective_user)
            prospective_user.matches.add(current_user)
        else:
            current_user.prospects.add(prospective_user)

        return Response([int(str(val)) for val in current_user.matches.all()])


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
