import json
from channels.db import database_sync_to_async

from chat.models import Message, Room


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

    message = data_json['message']
    message_content = data



    return message
