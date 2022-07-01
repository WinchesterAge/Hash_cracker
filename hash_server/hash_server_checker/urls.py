from django.urls import path,include
from .views import *
urlpatterns = [
    path('hash_api',hash_serializer_view),
    path('hash_checker/<Hash>/<hash_type>',hash_checker)
]
