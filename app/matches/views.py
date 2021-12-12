from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
