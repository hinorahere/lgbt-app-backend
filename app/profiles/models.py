from django.db import models


class Photo(models.Model):
    name = models.CharField(max_length=40)
    photo = models.FileField(blank=True, null=True, upload_to='')

    def __str__(self):
        return self.name



class Profile(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=2000)
    profile_picture = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name + ", " + self.first_name
