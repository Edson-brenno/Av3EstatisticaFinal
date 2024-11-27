from django.shortcuts import render, redirect
from home.models import PesquisaDados, PesquisaResposta

#perguntas referente ao projeto
from home.form_perguntas import perguntas_form
# Create your views here.

#pagina principal do projeto
def home(request, pergunta, id_pessoa=None):
    try:
        pessoa = PesquisaDados.objects.get(id=id_pessoa)
        perguntas_respondidas = PesquisaResposta.objects.values_list('pergunta').filter(id_pessoa=id_pessoa)
        perguntas_respondidas = [n[0] for n in perguntas_respondidas]
    except (PesquisaResposta.DoesNotExist,PesquisaDados.DoesNotExist):
        perguntas_respondidas = None
    if request.method == 'POST':
        if pergunta == 0:
            nome = request.POST.get('nome')
            idade = request.POST.get('idade')
            resgistro = PesquisaDados(nome=nome,idade=idade)
            resgistro.save()
            id_pessoa=resgistro.id
        else:
            form_resposta = request.POST.get('pergunta')
            if pergunta not in perguntas_respondidas:
                pessoa = PesquisaDados.objects.get(id=id_pessoa)
                db_resposta = PesquisaResposta(id_pessoa=pessoa, resposta=form_resposta, pergunta=pergunta)
                db_resposta.save()
            else:
                pessoa = PesquisaDados.objects.get(id=id_pessoa)
                db_resposta = PesquisaResposta.objects.get(id_pessoa=pessoa,pergunta=pergunta)
                db_resposta.resposta = form_resposta
                db_resposta.save()

        if pergunta+1 >= len(perguntas_form):
            return render(request,'fim.html')
        return redirect('form', pergunta=pergunta+1, id_pessoa=id_pessoa)
    
    if id_pessoa == None and pergunta >= 1 :
        return redirect('home', pergunta=0)
    
    return render(request,'home.html', context={'questao': perguntas_form[pergunta]['pergunta'],'alternativas': perguntas_form[pergunta]['alternativas'] , 'pergunta': f'Pergunta {pergunta}', 'perguntas': range(len(perguntas_form)), 'numero': pergunta,'id_pessoa':id_pessoa,'perguntas_respondidas': perguntas_respondidas})

def relatorio(request):
    
    return render(request,'relatorio.html')

def error404(*request):
    redirect('home', pergunta=1)
    return redirect('home', pergunta=1)