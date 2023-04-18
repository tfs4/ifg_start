from django.db import models


class PessoaModel(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome



class VistoriaModel(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome



class CarroModel(models.Model):
    nome = models.CharField(max_length=200)
    placa = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    pessoa = models.ForeignKey(PessoaModel, related_name="pessoa_carro", on_delete=models.CASCADE)
    # vistoria = models.ManyToManyField(VistoriaModel)


    def __str__(self):
        return self.nome



