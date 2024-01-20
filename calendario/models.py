from django.db import models
from django.urls import reverse


class Compromisso(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("compromisso_detail", args=[str(self.id)])
