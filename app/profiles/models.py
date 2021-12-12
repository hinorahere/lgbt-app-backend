from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.last_name + ", " + self.first_name
