from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from accounts import views


urlpatterns = [
    path('get_user/', views.get_user),
]


urlpatterns = format_suffix_patterns(urlpatterns)
