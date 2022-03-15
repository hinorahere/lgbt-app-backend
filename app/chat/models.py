from django.db import models

from django.conf import settings


class Room(models.Model):
    user_1 = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='+',
                                on_delete=models.CASCADE)

    user_2 = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='+',
                                on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user_1) + ", " + str(self.user_2)


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='+',
                              on_delete=models.CASCADE)

    message = models.CharField(max_length=2000)
    room = models.ForeignKey(Room, related_name='+', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
