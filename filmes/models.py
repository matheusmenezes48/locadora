from django.db import models

class Filme(models.Model):
    nome = models.CharField(max_length=50)
    dt_lancamento = models.DateField()
    sinopse = models.CharField(max_length=700)
    genero = models.CharField(max_length=20)
    

class Serie(models.Model):
    nome = models.CharField(max_length=50)
    dt_lancamento = models.DateField()
    sinopse = models.CharField(max_length=700)
    quant_temporadas = models.CharField(max_length=2)
    genero = models.CharField(max_length=20)