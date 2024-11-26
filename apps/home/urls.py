from django.urls import path
from django.shortcuts import redirect
from .views import home

urlpatterns = [
    path('', lambda request: redirect('home', pergunta=1)),
    path('<int:pergunta>', home, name='home'),
    path('<int:pergunta>/<int:id_pessoa>', home, name='form'),
]