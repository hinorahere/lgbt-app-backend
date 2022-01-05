from django.contrib import admin

from .models import Photo, Profile


class PhotoAdmin(admin.ModelAdmin):
    field = ('photo',)
    list_display = ('id', 'photo',)

class ProfileAdmin(admin.ModelAdmin):
    fields = ('first_name','last_name', 'bio', 'profile_picture',)
    list_display = ('id', 'first_name','last_name', 'bio', 'profile_picture',)


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Profile, ProfileAdmin)
