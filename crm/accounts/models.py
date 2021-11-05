from django.db import models

# Create your models here.


class User(models.Model):
    nome = models.CharField(max_length=255, null=True)
    telefone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nome


class Aviso(models.Model):
    PRIORIDADE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    titulo = models.CharField(max_length=255, null=True)
    conteudo = models.CharField(max_length=255, null=True)
    prioridade = models.CharField(
        max_length=255, null=True, choices=PRIORIDADE)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    data_validade = models.DateTimeField(null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.titulo


# onde irei criar todas as variaveis do BD para implementação das tabelas e envolvimento de dados
