from django.shortcuts import render

# Create your views here.
def relatorio(request):

    return render(request, 'relatorio/relatorio.html', context={'relatorio': True})