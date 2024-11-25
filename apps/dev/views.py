from django.shortcuts import render

# Create your views here.

#pagina para os desenvolvedores do projeto
def dev(request):
    return render(request,'dev.html')