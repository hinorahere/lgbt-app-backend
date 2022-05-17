from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse


from .models import Message
from .services.db import get_room

def index(request):
    '''
    Function just for testing backend
    Chat rooms rendered on the Flutter frontend
    '''
    return render(request, 'chat/index.html')


def room(request, room_name):
    '''
    Function just for testing backend
    Chat rooms rendered on the Flutter frontend
    '''
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


# Create serializer!!!!! and remove safe=False ******************
@api_view(['GET'])
def get_messages(request, room_id):
    '''
    Function returns previous messages between current user and matched user
    '''
    if request.method == 'GET':
        room = get_room(room_id)
        try:
            messages = Message.objects.filter(room=room).values().order_by('created_at')
        except Exception as error:
            raise Exception(repr(error))

        return JsonResponse(list(messages), safe=False)
