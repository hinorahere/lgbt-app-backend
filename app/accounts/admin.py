from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    fields = ('username',
              'email',
              'profile',
              'matches',
              'prospects',
              'rejects')
    list_display = ('id', 'email', 'profile')


admin.site.register(CustomUser, CustomUserAdmin)
