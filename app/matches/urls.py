from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from matches import views

urlpatterns = [
    path('match_check/', views.match_check),
    path('match_decline/', views.match_decline),
    path('match_remove/', views.match_remove),
    path('match_list/', views.match_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
