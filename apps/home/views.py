from django.shortcuts import render, redirect
from home.models import PesquisaDados, PesquisaResposta

# Create your views here.
#perguntas referente ao projeto
perguntas = [
        {'pergunta':'Qual o seu nome completo, e a sua idade ?\nObs: Antes de darmos prosseguimento um pedido dos desenvolvedores é que você não saia sem antes de terminar de responder toda a pesquisa. Agradecemos desde já.', 'alternativas':'input init'},
        
        {'pergunta':'Em uma escala de 1 a 5, com que frequência você realiza ações em casa para proteger o meio ambiente (ex.: separar o lixo, evitar produtos não recicláveis) ?', 'alternativas':['Altíssima Frequência','Alta Frequência', 'Frequente', 'Baixa Frequência', 'Baixíssima Frequência']},
                 
        {'pergunta':'Em uma escala de 1 a 5, com que frequência você evita o uso de plásticos descartáveis para reduzir a poluição dos oceanos ?', 'alternativas':['Altíssima Frequência','Alta Frequência', 'Frequente', 'Baixa Frequência', 'Baixíssima Frequência']},

        {'pergunta':'Em uma escala de 1 a 5, quanto você considera importante preservar os oceanos para o futuro ?', 'alternativas':['Altíssima importância','Alta importância', 'Importante', 'Baixa importância', 'Baixíssima importância']},

        {'pergunta':'Em uma escala de 1 a 5, qual é a sua percepção sobre as ações do governo para proteger a vida marinha ?', 'alternativas':['Altamente Suficiente','Muito Suficiente', 'Suficiente', 'Pouco Suficiente', 'Nada Suficiente']},

        {'pergunta':'Em uma escala de 1 a 5, qual é a sua percepção sobre as ações das empresas para proteger a vida marinha ?', 'alternativas':['Altamente Suficiente','Muito Suficiente', 'Suficiente', 'Pouco Suficiente', 'Nada Suficiente']},

        {'pergunta':'Na sua opinião, qual dessas ações é mais importante para proteger os oceanos ?', 'alternativas':['Reduzir o uso de plásticos',' Aumentar campanhas de conscientização', 'Incentivar práticas de pesca sustentável', 'Reforçar leis de proteção ambiental', 'Melhorar o saneamento básico para evitar esgoto nos oceanos']},

        {'pergunta':'Quantos KG de lixo você produz por mês ?', 'alternativas':'input valor'},

        {'pergunta':'Por que a preservação dos ecossistemas costeiros e marinhos é essencial para a segurança alimentar global e como a pesca sustentável pode contribuir para isso ?', 'alternativas':'input texto'},

        {'pergunta':'Quais são as principais fontes de poluição nos oceanos e mares, e como a redução dessas fontes pode impactar positivamente a biodiversidade aquática ?', 'alternativas':'input texto'},

        {'pergunta':'De que forma a redução da acidificação dos oceanos pode ajudar no combate às mudanças climáticas e na preservação da vida marinha ?', 'alternativas':'input texto'},
    ]
#pagina principal do projeto
def home(request, pergunta, id_pessoa=None):

    if request.method == 'POST':
        if pergunta == 0:
            nome = request.POST.get('nome')
            idade = request.POST.get('idade')
            resgistro = PesquisaDados(nome=nome,idade=idade)
            resgistro.save()
            id_pessoa=resgistro.id
        else:
            resposta = request.POST.get('pergunta')
            pessoa = PesquisaDados.objects.get(id=id_pessoa)
            resposta = PesquisaResposta(id_pessoa=pessoa, resposta=resposta, pergunta=pergunta-1)
            resposta.save()
        if pergunta+1 >= len(perguntas):
            return render(request,'fim.html')
        return redirect('form', pergunta=pergunta+1, id_pessoa=id_pessoa)
    if id_pessoa == None and pergunta >= 1 :
        return redirect('home', pergunta=0)
    if id_pessoa is not None:
        try:
            pessoa = PesquisaDados.objects.get(id=id_pessoa)
            respondidas = PesquisaResposta.objects.values_list('pergunta').filter(id_pessoa=id_pessoa)
            respondidas = [n[0]+1 for n in respondidas]
        except PesquisaResposta.DoesNotExist:
            pass
    else:
        respondidas = None
    return render(request,'home.html', context={'questao': perguntas[pergunta]['pergunta'],'alternativas': perguntas[pergunta]['alternativas'] , 'pergunta': f'Pergunta {pergunta}', 'perguntas': range(len(perguntas)), 'numero': pergunta,'id_pessoa':id_pessoa,'perguntas_respondidas': respondidas})

def error404(*request):
    redirect('home', pergunta=1)
    return redirect('home', pergunta=1)