from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from profiles import views

urlpatterns = [
    path('profile/', views.UserProfile.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)