from django.contrib import admin

from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    fields = ('email',
              'profile',
              'matches',
              'prospects')
    list_display = ('id', 'email', 'profile')


admin.site.register(CustomUser, CustomUserAdmin)
