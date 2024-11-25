from django.shortcuts import render, redirect


# Create your views here.

#pagina principal do projeto
def home(request, pergunta):
    perguntas = ['Em uma escala de 1 a 5, com que frequência você realiza ações em casa para proteger o meio ambiente (ex.: separar o lixo, evitar produtos não recicláveis) ?',
                 'Em uma escala de 1 a 5, com que frequência você evita o uso de plásticos descartáveis para reduzir a poluição dos oceanos ?',
                 'Em uma escala de 1 a 5, quanto você considera importante preservar os oceanos para o futuro ?',
                 'Em uma escala de 1 a 5, qual é a sua percepção sobre as ações do governo para proteger a vida marinha ?',
                 'Em uma escala de 1 a 5, qual é a sua percepção sobre as ações das empresas para proteger a vida marinha ?',
                 'Na sua opinião, qual dessas ações é mais importante para proteger os oceanos ?',
                 'Quantos KG de lixo você produz por mês ?']
    if request.method == 'POST':
        resposta = request.POST.get('pergunta')
        if pergunta == len(perguntas):
            return render(request,'fim.html')
        return redirect('home', pergunta=pergunta+1)

    return render(request,'home.html', context={'questao': perguntas[pergunta - 1], 'pergunta': f'Pergunta {pergunta}', 'perguntas': range(1,len(perguntas)+1), 'numero': pergunta},)

def error404(*request):
    redirect('home', pergunta=1)
    return redirect('home', pergunta=1)