from django.urls import path
from django.shortcuts import redirect
from .views import home,relatorio

urlpatterns = [
    path('home/', lambda request: redirect('home', pergunta=0)),
    path('relatorio/', relatorio, name='relatorio'),
    path('<int:pergunta>', home, name='home'),
    path('<int:pergunta>/<int:id_pessoa>', home, name='form'),
]