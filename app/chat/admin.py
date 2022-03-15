from django.contrib import admin

from .models import Message, Room


class RoomAdmin(admin.ModelAdmin):
    field = ('user_1', 'user_2')
    list_display = ('id', 'user_1', 'user_2',)

class MessageAdmin(admin.ModelAdmin):
    fields = ('message','room', 'user')
    list_display = ('id', 'message','room', 'user', 'created_at')


admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
