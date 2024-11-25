from django.shortcuts import render

# Create your views here.

#pagina de login do projeto
def entrar(request):
    return render(request,'login.html')