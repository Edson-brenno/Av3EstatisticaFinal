from django.db import models
# Create your models here.

class PesquisaDados(models.Model):
    nome = models.CharField(max_length=255)  # Coluna para um texto com limite de 255 caracteres
    idade = models.IntegerField() # Coluna para um número inteiro
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data de criação automática

    def __str__(self):
        return self.nome  # Representação legível do objeto

class PesquisaResposta(models.Model):
    id_pessoa = models.ForeignKey(PesquisaDados, on_delete=models.CASCADE)  # Chave estrangeira
    pergunta = models.IntegerField() # Coluna para um número inteiro
    resposta = models.CharField(max_length=255)

