from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    fields = ('username',
              'email',
              'profile',
              'matches',
              'prospects',
              'rejects')
    list_display = ('id', 'username', 'email', 'profile')


admin.site.register(CustomUser, CustomUserAdmin)
