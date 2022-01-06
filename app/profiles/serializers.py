from rest_framework import serializers

from .models import Photo, Profile


class PhotoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Photo
        fields = ('id',
                  'name',
                  'photo',
              )



class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ('id',
                  'first_name',
                  'last_name',
                  'bio',
                  'profile_picture',
              )



