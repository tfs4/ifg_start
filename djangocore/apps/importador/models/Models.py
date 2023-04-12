from django.db import models

#get_budget() - Budget Execution Summary Report
TIPO_SERVICO_ESSENCIAL = [
    ('RREO', 'Relatório Resumido de Execução Orçamentária - RREO'),
    ('EAC', 'Extrato Anual de Contas - EAC'),
    ('RGF', 'Relatório de Gestão Fiscal - RGF')
]

ANO = [
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
]

BIMESTRE = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
]

ESTADOS = [
    ('12','Acre - AC'),
    ('27','Alagoas - AL'),
    ('16','Amapá - AP'),
    ('13','Amazonas - AM'),
    ('29','Bahia - BA'),
    ('23','Ceará - CE'),
    ('53','Distrito Federal - DF'),
    ('32','Espírito Santo - ES'),
    ('52','Goiás - GO'),
    ('21','Maranhão - MA'),
    ('51','Mato Grosso - MT'),
    ('50','Mato Grosso do Sul - MS'),
    ('31','Minas Gerais - MG'),
    ('15','Pará - PA'),
    ('25','Paraíba - PB'),
    ('41','Paraná - PR'),
    ('26','Pernambuco - PE'),
    ('22','Piauí - PI'),
    ('24','Rio Grande do Norte - RN'),
    ('43','Rio Grande do Sul - RS'),
    ('33','Rio de Janeiro - RJ'),
    ('11','Rondônia - RO'),
    ('14','Roraima - RR'),
    ('42','Santa Catarina - SC'),
    ('35','São Paulo - SP'),
    ('28','Sergipe - SE'),
    ('17','Tocantins - TO'),
]





class ImportacaoModel(models.Model):
    class Meta:
        verbose_name = "Importar Dados"
        permissions = (
            ("importar_dados", "Pode Importar Dados"),
        )

    tipo_relatorio = models.CharField(max_length=25, null=True, blank=True, choices=TIPO_SERVICO_ESSENCIAL)
    ano = models.CharField(max_length=25, null=True, blank=True, choices=ANO)
    bimestre = models.CharField(max_length=25, null=True, blank=True, choices=BIMESTRE)
    estado = models.CharField(max_length=25, null=True, blank=True, choices=ESTADOS)


# ,exercicio,instituicao,cod_ibge,uf,anexo,rotulo,coluna,cod_conta,conta,valor,populacao
class EACModel(models.Model):

    class Meta:
        verbose_name = "EAC"
        permissions = (
            ("eac", "EAC"),
        )

    exercicio = models.CharField(max_length=100, null=True, default='')
    instituicao = models.CharField(max_length=100, null=True, default='')
    cod_ibge = models.CharField(max_length=100, null=True, default='')
    uf = models.CharField(max_length=100, null=True, default='')
    anexo = models.CharField(max_length=100, null=True, default='')
    rotulo = models.CharField(max_length=100, null=True, default='')
    coluna = models.CharField(max_length=100, null=True, default='')
    cod_conta = models.CharField(max_length=100, null=True, default='')
    conta = models.CharField(max_length=100, null=True, default='')
    valor = models.CharField(max_length=100, null=True, default='')
    populacao = models.CharField(max_length=100, null=True, default='')
    importacao = models.ForeignKey(ImportacaoModel, related_name="importacao_EAC", null=True, on_delete=models.CASCADE)



#,exercicio,periodo,periodicidade,instituicao,cod_ibge,uf,co_poder,populacao,anexo,esfera,rotulo,coluna,cod_conta,conta,valor
class RGFModel(models.Model):


    class Meta:
        verbose_name = "RGF"
        permissions = (
            ("rgf", "RGF"),
        )

    exercicio = models.CharField(max_length=100, null=True, default='')
    periodo = models.CharField(max_length=100, null=True, default='')
    periodicidade = models.CharField(max_length=100, null=True, default='')
    instituicao = models.CharField(max_length=100, null=True, default='')
    cod_ibge = models.CharField(max_length=100, null=True, default='')
    uf = models.CharField(max_length=100, null=True, default='')
    co_poder = models.CharField(max_length=100, null=True, default='')
    populacao = models.CharField(max_length=100, null=True, default='')
    anexo = models.CharField(max_length=100, null=True, default='')
    esfera = models.CharField(max_length=100, null=True, default='')
    rotulo = models.CharField(max_length=100, null=True, default='')
    coluna = models.CharField(max_length=100, null=True, default='')
    cod_conta = models.CharField(max_length=100, null=True, default='')
    conta = models.CharField(max_length=100, null=True, default='')
    valor = models.CharField(max_length=100, null=True, default='')
    importacao = models.ForeignKey(ImportacaoModel, related_name="importacao_RGF", null=True, on_delete=models.CASCADE)





class RREOModel(models.Model):


    class Meta:
        verbose_name = "RREO"
        permissions = (
            ("rreo", "RREO"),
        )

    exercicio = models.CharField(max_length=100, null=True, default='')
    demonstrativo = models.CharField(max_length=100, null=True, default='')
    periodo = models.CharField(max_length=100, null=True, default='')
    periodicidade = models.CharField(max_length=100, null=True, default='')
    instituicao = models.CharField(max_length=100, null=True, default='')
    cod_ibge = models.CharField(max_length=100, null=True, default='')
    uf = models.CharField(max_length=100, null=True, default='')
    populacao = models.CharField(max_length=100, null=True, default='')
    anexo = models.CharField(max_length=100, null=True, default='')
    esfera = models.CharField(max_length=100, null=True, default='')
    rotulo = models.CharField(max_length=100, null=True, default='')
    coluna = models.CharField(max_length=100, null=True, default='')
    cod_conta = models.CharField(max_length=100, null=True, default='')
    conta = models.CharField(max_length=100, null=True, default='')
    valor = models.CharField(max_length=100, null=True, default='')
    importacao = models.ForeignKey(ImportacaoModel, related_name="importacao_RREO", null=True, on_delete=models.CASCADE)
