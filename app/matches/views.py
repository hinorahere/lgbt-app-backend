from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings

from accounts.models import CustomUser as User

# {"id":5}
@api_view(['POST'])
def match(request):
    if request.method == 'POST':
        if not isinstance(request.data["prospective_id"], int):
            raise TypeError("prospective_id must be of type int")

        try:
            current_user = User.objects.get(id=request.user.id)
            prospective_id = int(request.data["prospective_id"])
        except Exception as error:
            raise Exception(repr(error))

        match = False
        for prospect in current_user.prospects.all():
            if int(str(prospect)) == prospective_id:
                match = True
                break

        return Response(match)

    return Response(request, status=405)


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
