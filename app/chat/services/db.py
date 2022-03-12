import json
from channels.db import database_sync_to_async

from chat.models import Message, Room
from matches.services import get_user

def get_room(room_id):
    try:
        room = Room.objects.get(id=room_id)
    except Exception as error:
        raise Exception(repr(error))

    return room


@database_sync_to_async
def save_message(data):
    if not data: return ''
    null_check = False

    data_json = json.loads(data)

    for key, value in data_json.items():
        if not value:
            null_check = True

    if null_check:
        return ''

    user = get_user(data_json['user_id'])
    room = get_room(1)
    message_data = Message(user=user,
                           message=data_json['message'],
                           room=room)
    message_data.save()

    return data_json['message']
