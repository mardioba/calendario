# /home/mardio/Projetos/calendario/calendario/models.py
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Compromisso(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.TextField()
    concluido = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("compromisso_detail", args=[str(self.id)])
