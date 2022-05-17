from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .services import get_user


@api_view(['POST'])
def match_decline(request):
    '''
    Function allows current user to reject a prospective user
    and puts both users on each others reject list

    Authorization Token Required

    Sample Body:
        {
            "prospective_id": 3
        }
    '''
    if request.method == 'POST':
        current_user = get_user(request.user.id)
        prospective_user = get_user(int(request.data["prospective_id"]))

        if not prospective_user:
            return Response("Declined Prospect")

        current_user.prospects.remove(prospective_user)
        prospective_user.prospects.remove(current_user)
        current_user.matches.remove(prospective_user)
        prospective_user.matches.remove(current_user)

        current_user.rejects.add(prospective_user)
        prospective_user.rejects.add(current_user)

        return Response("Declined Prospect")


@api_view(['POST'])
def match_check(request):
    """
        Function determines whether or not the passed prospective user ID is a
        match.

        Authorization Token Required

        Sample Body:
            {
                "prospective_id": 3
            }
    """
    if request.method == 'POST':
        # Type check(s)
        if not isinstance(request.data["prospective_id"], int):
            raise TypeError("prospective_id must be of type int")

        # Get users
        current_user = get_user(request.user.id)
        prospective_user = get_user(int(request.data["prospective_id"]))

        if not prospective_user:
            return Response({"matches": [int(str(val)) \
                                        for val in current_user.matches.all()]})

        # Check if current user is in prospective user's
        # rejection list
        for user_id in prospective_user.rejects.all():
            if int(str(user_id)) == request.user.id:
                current_user.rejects.add(prospective_user)
                return Response(False)

        # Determine if users are a match
        match = False
        for user_id in prospective_user.prospects.all():
            if int(str(user_id)) == current_user.id:
                match = True
                break

        # If match, update match fields on both users
        # else add prospective user to current_users prospective list
        if match:
            current_user.matches.add(prospective_user)
            prospective_user.matches.add(current_user)
            current_user.prospects.remove(prospective_user)
            prospective_user.prospects.remove(current_user)
        else:
            current_user.prospects.add(prospective_user)

        return Response({"matches": [int(str(val)) \
                                        for val in current_user.matches.all()]})


@api_view(['DELETE'])
def match_remove(request):
    '''
    Function allows current user to remove an already match user. Adds
    both users to each other's reject list

    Authorization Token Required

    Sample Body:
        {
            "prospective_id": 3
        }
    '''
    if request.method == 'DELETE':
        current_user = get_user(request.user.id)
        prospective_user = get_user(int(request.data["prospective_id"]))

        if not prospective_user:
            return Response("Match Removed")

        current_user.matches.remove(prospective_user)
        prospective_user.matches.remove(current_user)

        current_user.prospects.remove(prospective_user)
        prospective_user.prospects.remove(current_user)

        current_user.rejects.add(prospective_user)
        prospective_user.rejects.add(current_user)

        return Response("Removed")


@api_view(['GET'])
def match_list(request):
    '''
    Fucntion returns current user's match list

    Authorization Token Required

    Sample Body:
        {
            "prospective_id": 3
        }
    '''
    if request.method == 'GET':
        current_user = get_user(request.user.id)
        return Response([int(str(val)) for val in current_user.matches.all()])
