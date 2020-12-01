from django.urls import path
from .views import search_retake, get_disciplines, get_teachers, get_groups, RetakeListing


urlpatterns = [
    path('', search_retake, name='search_retake'),
    path('retake_listing', RetakeListing.as_view(), name='listing'),
    path('ajax/disciplines', get_disciplines, name='get_disciplines'),
    path('ajax/teachers', get_teachers, name='get_teachers'),
    path('ajax/groups', get_groups, name='get_groups'),
]