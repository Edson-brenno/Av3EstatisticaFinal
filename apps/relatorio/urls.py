from django.urls import path

from apps.relatorio import views

urlpatterns = [
    path('relatorio/estatistico/', views.relatorio, name='relatorio'),
]