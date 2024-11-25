from django.shortcuts import render

# Create your views here.

#pagina para cadastro do projeto(somente os adms usaram)
def registrar(request):
    return render(request,'cadastro.html')