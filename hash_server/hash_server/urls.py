from .views import redirecter
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("hash_server_checker.urls")),
    path('',redirecter)
]
