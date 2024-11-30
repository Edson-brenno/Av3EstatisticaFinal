from django.http import JsonResponse
from django.shortcuts import render

from questionario.models import TbQuestionario


# Create your views here.
def relatorio(request):

    return render(request, 'relatorio/relatorio.html', context={'relatorio': True})

def obter_dados_grafico(request):

    dados = TbQuestionario.objects.all()

    dados_retorno_grafico = {
        "grafico_questao_1": {
            "altissima_frequencia": dados.filter(questao_1 = 1).count(),
            "alta_frequencia": dados.filter(questao_1 = 2).count(),
            "frequente": dados.filter(questao_1 = 3).count(),
            "baixa_frequencia": dados.filter(questao_1 = 4).count(),
            "baixissima_frequencia": dados.filter(questao_1 = 5).count(),
        },
        "grafico_questao_2": {
            "altissima_frequencia": dados.filter(questao_2=1).count(),
            "alta_frequencia": dados.filter(questao_2=2).count(),
            "frequente": dados.filter(questao_2=3).count(),
            "baixa_frequencia": dados.filter(questao_2=4).count(),
            "baixissima_frequencia": dados.filter(questao_2=5).count(),
        },
        "grafico_questao_3": {
            "altissima_importancia": dados.filter(questao_3=1).count(),
            "alta_importancia": dados.filter(questao_3=2).count(),
            "importante": dados.filter(questao_3=3).count(),
            "baixa_importancia": dados.filter(questao_3=4).count(),
            "baixissima_importancia": dados.filter(questao_3=5).count(),
        },
        "grafico_questao_4": {
            "altamente_suficiente": dados.filter(questao_4=1).count(),
            "muito_suficiente": dados.filter(questao_4=2).count(),
            "suficiente": dados.filter(questao_4=3).count(),
            "pouco_suficiente": dados.filter(questao_4=4).count(),
            "nada_suficiente": dados.filter(questao_4=5).count(),
        },
        "grafico_questao_5": {
            "altamente_suficiente": dados.filter(questao_5=1).count(),
            "muito_suficiente": dados.filter(questao_5=2).count(),
            "suficiente": dados.filter(questao_5=3).count(),
            "pouco_suficiente": dados.filter(questao_5=4).count(),
            "nada_suficiente": dados.filter(questao_5=5).count(),
        },
        "grafico_questao_6": {
            "reduzir_uso_de_plastico": dados.filter(questao_6=1).count(),
            "aumentar_campanhas": dados.filter(questao_6=2).count(),
            "incentivar_particas": dados.filter(questao_6=3).count(),
            "reforcar_leis": dados.filter(questao_6=4).count(),
            "melhorar_saneamento": dados.filter(questao_6=5).count(),
        },
    }

    return JsonResponse(data=dados_retorno_grafico, safe=False)