from django.db import models
from django.contrib.auth.models import User


PAGAMENTO = [
    ('RECURSOS DA EMPRESA', 'RECURSOS DA EMPRESA'),
    ('RECURSOS PRÓPRIOS', 'RECURSOS PRÓPRIOS'),
]

BOOLEANO = [
    ('1', 'SIM'),
    ('0', 'NAO'),
]

class TiposDeViagemModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class TiposDeSolicitacaoModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class MotivoDeViagemModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class TipoDeTransporteModel(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome





class ViagemModel(models.Model):
    solicitante = models.ForeignKey(User, related_name="viagem_user", on_delete=models.CASCADE, null=True, blank=True)
    valor_passagem = models.CharField(max_length=200)
    dada_inicio = models.DateTimeField()
    dada_fim = models.DateField()
    origem = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    objetivo = models.CharField(max_length=200)
    tipo_viagem = models.ForeignKey(TiposDeViagemModel, related_name="viagem_tipo", on_delete=models.CASCADE)
    tipo_solicitacao = models.ForeignKey(TiposDeViagemModel, related_name="viagem_solicitacao",
                                         on_delete=models.CASCADE)
    motivo = models.ForeignKey(MotivoDeViagemModel, related_name="viagem_motivo", on_delete=models.CASCADE)
    tipo_transporte = models.ForeignKey(TipoDeTransporteModel, related_name="viagem_transporte",
                                        on_delete=models.CASCADE)
    autorizada = models.BooleanField(default=False)
    homologada = models.BooleanField(default=False)
    pagamento = models.CharField(max_length=50, null=True, blank=True, choices=PAGAMENTO)
    descricao = models.TextField(blank=True, null=True)
    finalizar_pc = models.CharField(max_length=50, null=True, blank=True, choices=BOOLEANO, default='0')

    def __str__(self):
        return self.origem+' - '+self.destino+' ( '+str(self.dada_inicio)+' - '+str(self.dada_fim)+' )'

    class Meta:
        verbose_name = "Viagens"
        permissions = (
            ("solicitar_viagens", "Pode solicitar viagens"),
            ("autorizar_viagens", "Pode autorizar viagens"),
            ("homologar_viagens", "Pode homologar viagens"),
            ("cadastrar_item_viagens", "Cadastrar Items de Viagem")
        )





class Arquivos(models.Model):
    descricao = models.TextField(blank=True, null=True)
    file =  models.FileField(upload_to='files/', null=True, blank=True)
    viagem = models.ForeignKey(ViagemModel, related_name="arquivos_viagem", null=True, on_delete=models.CASCADE)
