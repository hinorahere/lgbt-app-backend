from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from matches import views

urlpatterns = [
    path('match/', views.MatchList.as_view()),
    path('match/<int:pk>/', views.MatchDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
