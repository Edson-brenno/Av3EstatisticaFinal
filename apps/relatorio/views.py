from django.http import JsonResponse
from django.shortcuts import render

from questionario.models import TbQuestionario
import numpy as nb
from scipy import stats

# Create your views here.
def relatorio(request):

    return render(request, 'relatorio/relatorio.html', context={'relatorio': True})

def obter_dados_grafico(request):

    dados = TbQuestionario.objects.all()

    dados_retorno_grafico = {
        "grafico_questao_1": {
            "altissima_frequencia": dados.filter(questao_1 = 5).count(),
            "alta_frequencia": dados.filter(questao_1 = 4).count(),
            "frequente": dados.filter(questao_1 = 3).count(),
            "baixa_frequencia": dados.filter(questao_1 = 2).count(),
            "baixissima_frequencia": dados.filter(questao_1 = 1).count(),
        },
        "grafico_questao_2": {
            "altissima_frequencia": dados.filter(questao_2=5).count(),
            "alta_frequencia": dados.filter(questao_2=4).count(),
            "frequente": dados.filter(questao_2=3).count(),
            "baixa_frequencia": dados.filter(questao_2=2).count(),
            "baixissima_frequencia": dados.filter(questao_2=1).count(),
        },
        "grafico_questao_3": {
            "altissima_importancia": dados.filter(questao_3=5).count(),
            "alta_importancia": dados.filter(questao_3=4).count(),
            "importante": dados.filter(questao_3=3).count(),
            "baixa_importancia": dados.filter(questao_3=2).count(),
            "baixissima_importancia": dados.filter(questao_3=1).count(),
        },
        "grafico_questao_4": {
            "altamente_suficiente": dados.filter(questao_4=5).count(),
            "muito_suficiente": dados.filter(questao_4=4).count(),
            "suficiente": dados.filter(questao_4=3).count(),
            "pouco_suficiente": dados.filter(questao_4=2).count(),
            "nada_suficiente": dados.filter(questao_4=1).count(),
        },
        "grafico_questao_5": {
            "altamente_suficiente": dados.filter(questao_5=5).count(),
            "muito_suficiente": dados.filter(questao_5=4).count(),
            "suficiente": dados.filter(questao_5=3).count(),
            "pouco_suficiente": dados.filter(questao_5=2).count(),
            "nada_suficiente": dados.filter(questao_5=1).count(),
        },
        "grafico_questao_6": {
            "reduzir_uso_de_plastico": dados.filter(questao_6=5).count(),
            "aumentar_campanhas": dados.filter(questao_6=4).count(),
            "incentivar_particas": dados.filter(questao_6=3).count(),
            "reforcar_leis": dados.filter(questao_6=2).count(),
            "melhorar_saneamento": dados.filter(questao_6=1).count(),
        },
    }

    return JsonResponse(data=dados_retorno_grafico, safe=False)

# Função para converter numpy types em tipos nativos de Python
def converter_para_python(valor):
    if isinstance(valor, (nb.float64, nb.float32)):
        return float(valor)
    elif isinstance(valor, (nb.int64, nb.int32)):
        return int(valor)
    elif isinstance(valor, nb.ndarray):
        return valor.tolist()
    return valor

def obter_dados_dispersao(request):

    dados = TbQuestionario.objects.all()
    dados_dispersao_questao_1 = [dados.filter(questao_1=5).count(), dados.filter(questao_1=4).count(), dados.filter(questao_1=3).count(),
                                 dados.filter(questao_1=2).count(), dados.filter(questao_1=1).count()]

    dados_dispersao_questao_2 = [dados.filter(questao_2=5).count(), dados.filter(questao_2=4).count(),
                                 dados.filter(questao_2=3).count(),
                                 dados.filter(questao_2=2).count(), dados.filter(questao_2=1).count()]

    dados_dispersao_questao_3 = [dados.filter(questao_3=5).count(), dados.filter(questao_3=4).count(),
                                 dados.filter(questao_3=3).count(),
                                 dados.filter(questao_3=2).count(), dados.filter(questao_3=1).count()]

    dados_dispersao_questao_4 = [dados.filter(questao_4=5).count(), dados.filter(questao_4=4).count(),
                                 dados.filter(questao_4=3).count(),
                                 dados.filter(questao_4=2).count(), dados.filter(questao_4=1).count()]

    dados_dispersao_questao_5 = [dados.filter(questao_5=5).count(), dados.filter(questao_5=4).count(),
                                 dados.filter(questao_5=3).count(),
                                 dados.filter(questao_5=2).count(), dados.filter(questao_5=1).count()]

    dados_dispersao_questao_6 = [dados.filter(questao_6=5).count(), dados.filter(questao_6=4).count(),
                                 dados.filter(questao_6=3).count(),
                                 dados.filter(questao_6=2).count(), dados.filter(questao_6=1).count()]

    # Construindo os dados e convertendo os valores
    dados_retorno_dispersao = {
        "dispersao_questao_1": {
            "media": converter_para_python(nb.mean(dados_dispersao_questao_1)),
            "desvio_padrao": converter_para_python(nb.std(dados_dispersao_questao_1)),
            "desvio_medio": converter_para_python(
                nb.mean(nb.abs(dados_dispersao_questao_1 - nb.mean(dados_dispersao_questao_1)))),
            "variancia": converter_para_python(nb.var(dados_dispersao_questao_1)),
            "amplitude": converter_para_python(nb.max(dados_dispersao_questao_1) - nb.min(dados_dispersao_questao_1)),
        },
        "dispersao_questao_2": {
            "media": converter_para_python(nb.mean(dados_dispersao_questao_2)),
            "desvio_padrao": converter_para_python(nb.std(dados_dispersao_questao_2)),
            "desvio_medio": converter_para_python(
                nb.mean(nb.abs(dados_dispersao_questao_2 - nb.mean(dados_dispersao_questao_2)))),
            "variancia": converter_para_python(nb.var(dados_dispersao_questao_2)),
            "amplitude": converter_para_python(nb.max(dados_dispersao_questao_2) - nb.min(dados_dispersao_questao_2)),
        },
        "dispersao_questao_3": {
            "media": converter_para_python(nb.mean(dados_dispersao_questao_3)),
            "desvio_padrao": converter_para_python(nb.std(dados_dispersao_questao_3)),
            "desvio_medio": converter_para_python(
                nb.mean(nb.abs(dados_dispersao_questao_3 - nb.mean(dados_dispersao_questao_3)))),
            "variancia": converter_para_python(nb.var(dados_dispersao_questao_3)),
            "amplitude": converter_para_python(nb.max(dados_dispersao_questao_3) - nb.min(dados_dispersao_questao_3)),
        },
        "dispersao_questao_4": {
            "media": converter_para_python(nb.mean(dados_dispersao_questao_4)),
            "desvio_padrao": converter_para_python(nb.std(dados_dispersao_questao_4)),
            "desvio_medio": converter_para_python(
                nb.mean(nb.abs(dados_dispersao_questao_4 - nb.mean(dados_dispersao_questao_4)))),
            "variancia": converter_para_python(nb.var(dados_dispersao_questao_4)),
            "amplitude": converter_para_python(nb.max(dados_dispersao_questao_4) - nb.min(dados_dispersao_questao_4)),
        },
        "dispersao_questao_5": {
            "media": converter_para_python(nb.mean(dados_dispersao_questao_5)),
            "desvio_padrao": converter_para_python(nb.std(dados_dispersao_questao_5)),
            "desvio_medio": converter_para_python(
                nb.mean(nb.abs(dados_dispersao_questao_5 - nb.mean(dados_dispersao_questao_5)))),
            "variancia": converter_para_python(nb.var(dados_dispersao_questao_5)),
            "amplitude": converter_para_python(nb.max(dados_dispersao_questao_5) - nb.min(dados_dispersao_questao_5)),
        },
        "dispersao_questao_6": {
            "media": converter_para_python(nb.mean(dados_dispersao_questao_6)),
            "desvio_padrao": converter_para_python(nb.std(dados_dispersao_questao_6)),
            "desvio_medio": converter_para_python(
                nb.mean(nb.abs(dados_dispersao_questao_6 - nb.mean(dados_dispersao_questao_6)))),
            "variancia": converter_para_python(nb.var(dados_dispersao_questao_6)),
            "amplitude": converter_para_python(nb.max(dados_dispersao_questao_6) - nb.min(dados_dispersao_questao_6)),
        },
    }

    return JsonResponse(data=dados_retorno_dispersao, safe=False)

def obter_moda(dados):
    resultado_moda = stats.mode(dados, keepdims=True)
    return converter_para_python(resultado_moda.mode[0])

def obter_dados_tendencia(request):

    dados = TbQuestionario.objects.all()

    dados_tendencia_questao_1 = [dados.filter(questao_1=5).count(), dados.filter(questao_1=4).count(), dados.filter(questao_1=3).count(),
                                 dados.filter(questao_1=2).count(), dados.filter(questao_1=1).count()]

    dados_tendencia_questao_2 = [dados.filter(questao_2=5).count(), dados.filter(questao_2=4).count(),
                                 dados.filter(questao_2=3).count(),
                                 dados.filter(questao_2=2).count(), dados.filter(questao_2=1).count()]

    dados_tendencia_questao_3 = [dados.filter(questao_3=5).count(), dados.filter(questao_3=4).count(),
                                 dados.filter(questao_3=3).count(),
                                 dados.filter(questao_3=2).count(), dados.filter(questao_3=1).count()]

    dados_tendencia_questao_4 = [dados.filter(questao_4=5).count(), dados.filter(questao_4=4).count(),
                                 dados.filter(questao_4=3).count(),
                                 dados.filter(questao_4=2).count(), dados.filter(questao_4=1).count()]

    dados_tendencia_questao_5 = [dados.filter(questao_5=5).count(), dados.filter(questao_5=4).count(),
                                 dados.filter(questao_5=3).count(),
                                 dados.filter(questao_5=2).count(), dados.filter(questao_5=1).count()]

    dados_tendencia_questao_6 = [dados.filter(questao_6=5).count(), dados.filter(questao_6=4).count(),
                                 dados.filter(questao_6=3).count(),
                                 dados.filter(questao_6=2).count(), dados.filter(questao_6=1).count()]

    # Construindo os dados e convertendo os valores
    # Construindo os dados e convertendo os valores
    dados_retorno_tendencia = {
        "tendencia_questao_1": {
            "media": converter_para_python(nb.mean(dados_tendencia_questao_1)),
            "mediana": converter_para_python(nb.median(dados_tendencia_questao_1)),
            "moda": dados_tendencia_questao_1.index(max(dados_tendencia_questao_1)) + 1,
        },
        "tendencia_questao_2": {
            "media": converter_para_python(nb.mean(dados_tendencia_questao_2)),
            "mediana": converter_para_python(nb.median(dados_tendencia_questao_2)),
            "moda": dados_tendencia_questao_2.index(max(dados_tendencia_questao_2)) + 1,
        },
        "tendencia_questao_3": {
            "media": converter_para_python(nb.mean(dados_tendencia_questao_3)),
            "mediana": converter_para_python(nb.median(dados_tendencia_questao_3)),
            "moda": dados_tendencia_questao_3.index(max(dados_tendencia_questao_3)) + 1,
        },
        "tendencia_questao_4": {
            "media": converter_para_python(nb.mean(dados_tendencia_questao_4)),
            "mediana": converter_para_python(nb.median(dados_tendencia_questao_4)),
            "moda": dados_tendencia_questao_4.index(max(dados_tendencia_questao_4)) + 1,
        },
        "tendencia_questao_5": {
            "media": converter_para_python(nb.mean(dados_tendencia_questao_5)),
            "mediana": converter_para_python(nb.median(dados_tendencia_questao_5)),
            "moda": dados_tendencia_questao_5.index(max(dados_tendencia_questao_5)) + 1,
        },
        "tendencia_questao_6": {
            "media": converter_para_python(nb.mean(dados_tendencia_questao_6)),
            "mediana": converter_para_python(nb.median(dados_tendencia_questao_6)),
            "moda": dados_tendencia_questao_6.index(max(dados_tendencia_questao_6)) + 1,
        }
    }

    return JsonResponse(data=dados_retorno_tendencia, safe=False)