from django.urls import path

from apps.questionario.views import questionario

urlpatterns = [
    path('questionario/', questionario, name='questionario'),
]