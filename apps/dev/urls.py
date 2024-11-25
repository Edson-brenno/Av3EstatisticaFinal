from django.urls import path
from .views import dev

urlpatterns = [
    path('', dev, name='dev'),
]