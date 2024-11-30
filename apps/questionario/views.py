from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def questionario(request):

    print(request.body)
    return HttpResponse("<h1>Questionario</h1>")