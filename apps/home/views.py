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

    if request.method == 'POST':
        botao = request.POST.get('botao')
        match botao:
            case 'grafico':
                for n in range(1,7):
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
                    plt.xticks(rotation=45, fontsize=10)
                    plt.savefig(os.path.join(CAMINHO,'static','grafico',f'grafico{n}.png'), dpi=100, bbox_inches='tight')
                    plt.clf()
                return render(request,'relatorio.html',{'grafico':[f'grafico/grafico{i}.png' for i in range(1,7)]})
            case 'tendencia':
                data = pd.DataFrame(dados)
                for n in range(1,7):
                    colunas = data[(data['pergunta'] == n)]
                    valor = 5
                    for alternativa in perguntas_form[n]['alternativas']:
                        colunas['resposta']= colunas['resposta'].replace(alternativa,str(valor))
                        valor -= 1
                    colunas['resposta'] = colunas['resposta'].astype(int)
                    #tendencia central
                    media = colunas['resposta'].mean()
                    mediana = colunas['resposta'].median()
                    moda = stats.mode(colunas['resposta'])

                    plt.hist(colunas['resposta'], bins=5, color="skyblue", edgecolor="black", alpha=0.7)
                    plt.axvline(media, color="red", linestyle="dashed", linewidth=1, label=f"Média: {media:.2f}")
                    plt.axvline(mediana, color="green", linestyle="dashed", linewidth=1, label=f"Mediana: {mediana:.2f}")
                    plt.axvline(moda.mode, color="blue", linestyle="dashed", linewidth=1, label=f"Moda: {moda.mode}")
                    plt.title(f"Medidas de Tendencia Central Questão {n}")
                    plt.xlabel("Valores das Alternativas")
                    plt.ylabel("Frequências")
                    plt.legend()
                    plt.xticks(fontsize=10)
                    plt.savefig(os.path.join(CAMINHO,'static','tendencia',f'tendencia{n}.png'), dpi=100, bbox_inches='tight')
                    plt.clf()
                return render(request,'relatorio.html',{'tendencia':[f'tendencia/tendencia{i}.png' for i in range(1,7)]})
            case 'dispersao':
                data = pd.DataFrame(dados)
                for n in range(1,7):
                    colunas = data[(data['pergunta'] == n)]
                    valor = 5
                    for alternativa in perguntas_form[n]['alternativas']:
                        colunas['resposta']= colunas['resposta'].replace(alternativa,str(valor))
                        valor -= 1
                    colunas['resposta'] = colunas['resposta'].astype(int)
                    #dispersão
                    media = colunas['resposta'].mean()
                    desvio_medio = (colunas['resposta'] - media).abs().mean()
                    variancia = colunas['resposta'].var()
                    desvio_padrao = colunas['resposta'].std()
                    amplitude = colunas['resposta'].max() - colunas['resposta'].min()

                    plt.hist(colunas['resposta'], bins=8, color='skyblue', edgecolor='black', alpha=0.7)
                    plt.axvline(media, color='red', linestyle='--', label=f"Média: {media:.2f}")
                    plt.axvline(desvio_padrao, color='orange', linestyle='--', label=f"Desvio Padrão: {desvio_padrao:.2f}")
                    plt.axvline(desvio_medio, color='blue', linestyle='--', label=f"Desvio Médio: {desvio_medio:.2f}")
                    plt.axvline(variancia, color='black', linestyle='--', label=f"Variância: {variancia:.2f}")
                    plt.axvline(amplitude, color='green', linestyle='--', label=f"Amplitude: {amplitude:.2f}")
                    plt.title("Medidas de Dispersão")
                    plt.xlabel("Valores das Alternativas")
                    plt.ylabel("Frequência")
                    plt.legend()
                    plt.savefig(os.path.join(CAMINHO,'static','dispersao',f'dispersao{n}.png'), dpi=100, bbox_inches='tight')
                    plt.clf()
                return render(request,'relatorio.html',{'dispersao':[f'dispersao/dispersao{i}.png' for i in range(1,7)]})
            case 'tabela':
                data = pd.DataFrame(dados)
                tabela_all = data[['id_pessoa_id', 'pergunta', 'resposta']]
                tabela = []
                for n in range(1,11):
                    linhas = tabela_all[(tabela_all['pergunta'] == n)]
                    tabela.append(linhas)
                    for i in linhas.values:
                        print(i)
                print(tabela[0]['pergunta'])                        
                return render(request,'relatorio.html',{'tabela':tabela})       
    return render(request,'relatorio.html')

def error404(*request):
    redirect('home', pergunta=1)
    return redirect('home', pergunta=1)