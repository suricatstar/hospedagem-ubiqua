# Generated by Django 5.1.2 on 2024-10-22 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estrela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoAcomodacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoQuarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Acomodacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('capacidade', models.IntegerField()),
                ('imagem', models.ImageField(blank=True, upload_to='acomodacao/%Y/%m/%d')),
                ('estrelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acomodacao.estrela')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acomodacao.tipoacomodacao')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('hora_inicio', models.TimeField(blank=True, default='14:00:00')),
                ('data_fim', models.DateField()),
                ('hora_final', models.TimeField(blank=True, default='11:00:00')),
                ('quantidade_pessoas', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('acomodacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acomodacao.acomodacao')),
            ],
        ),
        migrations.CreateModel(
            name='AcomodacaoQuarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('quantidade_pessoas', models.IntegerField()),
                ('descricao', models.TextField()),
                ('diaria', models.DecimalField(decimal_places=2, max_digits=8)),
                ('acomodacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acomodacao.acomodacao')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acomodacao.tipoquarto')),
            ],
        ),
    ]
