from django.urls import path
from django.shortcuts import redirect
from .views import home

urlpatterns = [
    path('', lambda request: redirect('home', pergunta=0)),
    path('relatorio/', home, name='relatorio'),
    path('<int:pergunta>', home, name='home'),
    path('<int:pergunta>/<int:id_pessoa>', home, name='form'),
]