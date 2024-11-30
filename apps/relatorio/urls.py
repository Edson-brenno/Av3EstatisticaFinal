from django.urls import path

from apps.relatorio import views

urlpatterns = [
    path('relatorio/estatistico/', views.relatorio, name='relatorio'),
    path('relatorio/dados/grafico/', views.obter_dados_grafico, name='obter_dados_grafico'),
]