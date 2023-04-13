# Generated by Django 3.2.10 on 2023-02-03 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImportacaoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_relatorio', models.CharField(blank=True, choices=[('RREO', 'Relatório Resumido de Execução Orçamentária - RREO'), ('EAC', 'Extrato Anual de Contas - EAC'), ('RGF', 'Relatório de Gestão Fiscal - RGF')], max_length=25, null=True)),
                ('ano', models.CharField(blank=True, choices=[('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], max_length=25, null=True)),
                ('bimestre', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=25, null=True)),
                ('estado', models.CharField(blank=True, choices=[('12', 'Acre - AC'), ('27', 'Alagoas - AL'), ('16', 'Amapá - AP'), ('13', 'Amazonas - AM'), ('29', 'Bahia - BA'), ('23', 'Ceará - CE'), ('53', 'Distrito Federal - DF'), ('32', 'Espírito Santo - ES'), ('52', 'Goiás - GO'), ('21', 'Maranhão - MA'), ('51', 'Mato Grosso - MT'), ('50', 'Mato Grosso do Sul - MS'), ('31', 'Minas Gerais - MG'), ('15', 'Pará - PA'), ('25', 'Paraíba - PB'), ('41', 'Paraná - PR'), ('26', 'Pernambuco - PE'), ('22', 'Piauí - PI'), ('24', 'Rio Grande do Norte - RN'), ('43', 'Rio Grande do Sul - RS'), ('33', 'Rio de Janeiro - RJ'), ('11', 'Rondônia - RO'), ('14', 'Roraima - RR'), ('42', 'Santa Catarina - SC'), ('35', 'São Paulo - SP'), ('28', 'Sergipe - SE'), ('17', 'Tocantins - TO')], max_length=25, null=True)),
            ],
            options={
                'verbose_name': 'Importar Dados',
                'permissions': (('importar_dados', 'Pode Importar Dados'),),
            },
        ),
        migrations.CreateModel(
            name='RREOModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercicio', models.CharField(default='', max_length=100, null=True)),
                ('demonstrativo', models.CharField(default='', max_length=100, null=True)),
                ('periodo', models.CharField(default='', max_length=100, null=True)),
                ('periodicidade', models.CharField(default='', max_length=100, null=True)),
                ('instituicao', models.CharField(default='', max_length=100, null=True)),
                ('cod_ibge', models.CharField(default='', max_length=100, null=True)),
                ('uf', models.CharField(default='', max_length=100, null=True)),
                ('populacao', models.CharField(default='', max_length=100, null=True)),
                ('anexo', models.CharField(default='', max_length=100, null=True)),
                ('esfera', models.CharField(default='', max_length=100, null=True)),
                ('rotulo', models.CharField(default='', max_length=100, null=True)),
                ('coluna', models.CharField(default='', max_length=100, null=True)),
                ('cod_conta', models.CharField(default='', max_length=100, null=True)),
                ('conta', models.CharField(default='', max_length=100, null=True)),
                ('valor', models.CharField(default='', max_length=100, null=True)),
                ('importacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='importacao_RREO', to='importador.importacaomodel')),
            ],
            options={
                'verbose_name': 'RREO',
                'permissions': (('rreo', 'RREO'),),
            },
        ),
        migrations.CreateModel(
            name='RGFModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercicio', models.CharField(default='', max_length=100, null=True)),
                ('periodo', models.CharField(default='', max_length=100, null=True)),
                ('periodicidade', models.CharField(default='', max_length=100, null=True)),
                ('instituicao', models.CharField(default='', max_length=100, null=True)),
                ('cod_ibge', models.CharField(default='', max_length=100, null=True)),
                ('uf', models.CharField(default='', max_length=100, null=True)),
                ('co_poder', models.CharField(default='', max_length=100, null=True)),
                ('populacao', models.CharField(default='', max_length=100, null=True)),
                ('anexo', models.CharField(default='', max_length=100, null=True)),
                ('esfera', models.CharField(default='', max_length=100, null=True)),
                ('rotulo', models.CharField(default='', max_length=100, null=True)),
                ('coluna', models.CharField(default='', max_length=100, null=True)),
                ('cod_conta', models.CharField(default='', max_length=100, null=True)),
                ('conta', models.CharField(default='', max_length=100, null=True)),
                ('valor', models.CharField(default='', max_length=100, null=True)),
                ('importacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='importacao_RGF', to='importador.importacaomodel')),
            ],
            options={
                'verbose_name': 'RGF',
                'permissions': (('rgf', 'RGF'),),
            },
        ),
        migrations.CreateModel(
            name='EACModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercicio', models.CharField(default='', max_length=100, null=True)),
                ('instituicao', models.CharField(default='', max_length=100, null=True)),
                ('cod_ibge', models.CharField(default='', max_length=100, null=True)),
                ('uf', models.CharField(default='', max_length=100, null=True)),
                ('anexo', models.CharField(default='', max_length=100, null=True)),
                ('rotulo', models.CharField(default='', max_length=100, null=True)),
                ('coluna', models.CharField(default='', max_length=100, null=True)),
                ('cod_conta', models.CharField(default='', max_length=100, null=True)),
                ('conta', models.CharField(default='', max_length=100, null=True)),
                ('valor', models.CharField(default='', max_length=100, null=True)),
                ('populacao', models.CharField(default='', max_length=100, null=True)),
                ('importacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='importacao_EAC', to='importador.importacaomodel')),
            ],
            options={
                'verbose_name': 'EAC',
                'permissions': (('eac', 'EAC'),),
            },
        ),
    ]