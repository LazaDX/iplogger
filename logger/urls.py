from django.urls import path
from .views import track_ip

urlpatterns = [
    path('track/', track_ip, name='track_ip'),
]
