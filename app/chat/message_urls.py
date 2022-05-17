from django.urls import path

from . import views


urlpatterns = [
    path('messages/<str:room_id>/', views.get_messages),
]
