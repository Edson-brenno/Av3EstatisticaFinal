from django.http import HttpResponse
from django.shortcuts import render
from questionario.models import TbQuestionario

# Create your views here.
def questionario(request):

    if request.method == 'POST':
        email = request.POST['email']
        idade = int(request.POST['idade'])
        questao1 = int(request.POST['Questao1'])
        questao2 = int(request.POST['Questao2'])
        questao3 = int(request.POST['Questao3'])
        questao4 = int(request.POST['Questao4'])
        questao5 = int(request.POST['Questao5'])
        questao6 = int(request.POST['Questao6'])
        questao7 = int(request.POST['Questao7'])
        questao8 = request.POST['Questao8']
        questao9 = request.POST['Questao9']
        questao10 = request.POST['Questao10']

        if TbQuestionario.objects.filter(email=email).exists():
            return HttpResponse("Email ja existe")

        questionario = TbQuestionario(
            email=email,
            idade=idade,
            questao_1=questao1,  # Use the field name 'questao_1'
            questao_2=questao2,  # Use the field name 'questao_2'
            questao_3=questao3,
            questao_4=questao4,
            questao_5=questao5,
            questao_6=questao6,
            questao_7=questao7,
            questao_8=questao8,
            questao_9=questao9,
            questao_10=questao10
        )

        questionario.save()

        return HttpResponse("<h1>Questionario Salvo</h1>")