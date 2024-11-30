from django.db import models

# Create your models here.
class TbQuestionario(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False )
    email = models.EmailField(unique=True)
    idade = models.IntegerField(null=False)
    questao_1 = models.IntegerField(null=False)
    questao_2 = models.IntegerField(null=False)
    questao_3 = models.IntegerField(null=False)
    questao_4 = models.IntegerField(null=False)
    questao_5 = models.IntegerField(null=False)
    questao_6 = models.IntegerField(null=False)
    questao_7 = models.IntegerField(null=False)
    questao_8 = models.TextField(null=False, blank=False)
    questao_9 = models.TextField(null=False, blank=False)
    questao_10 = models.TextField(null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

        db_table = 'tb_questionario'