from django.shortcuts import render, redirect
from home.models import PesquisaDados, PesquisaResposta

from pathlib import Path
import os

CAMINHO = Path(__file__).parent.parent.parent

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Backend não interativo

import pandas as pd
import numpy as np
from scipy import stats

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
    dados_all = PesquisaResposta.objects.all()
    dados = []
    for dados_fil in dados_all:
        dados_fil.__dict__.pop('_state')
        dados.append(dados_fil.__dict__)

    if request.method == 'GET':
        grafico = request.POST.get('botao')
        grafico = '2'
        match grafico:
            case '1':
                for n in range(1,11):

                    data = {'resposta':[],'alternativas':perguntas_form[n]['alternativas'],'valor':[]}
                    print(data['alternativas'])
                    for dado in dados:
                        if n == dado['pergunta']:
                            data['valor'].append(dado['resposta'])
                    for resp in data['alternativas']:
                        data['resposta'].append(data['valor'].count(resp))
                    data.pop('valor')
                    sns.barplot(data=data,y='resposta',x='alternativas')
                    plt.title(f'Gráfico da Pergunta {n}')
                    plt.xticks(rotation=270, fontsize=10)
                    plt.tight_layout()
                    plt.savefig(os.path.join(CAMINHO,'static',f'arquivo{n}.png'), dpi=300, bbox_inches='tight')
                    plt.clf()
            case '2':
                data = pd.DataFrame(dados)

                # # Média
                # mean = data["resposta"].mean()
                # print(f"Média: {mean}")

                # # Mediana
                # median = data["Notas"].median()
                # print(f"Mediana: {median}")

                # # Moda
                # mode = stats.mode(data["Notas"])
                # print(f"Moda: {mode.mode[0]} (Frequência: {mode.count[0]})")
                print(data)
    return render(request,'relatorio.html')

def error404(*request):
    redirect('home', pergunta=1)
    return redirect('home', pergunta=1)