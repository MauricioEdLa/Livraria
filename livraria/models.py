from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    isbn = models.CharField(max_length=13)