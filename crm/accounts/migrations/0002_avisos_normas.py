# Generated by Django 3.2.8 on 2021-10-25 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, null=True)),
                ('conteudo', models.CharField(max_length=255, null=True)),
                ('prioridade', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=255, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, null=True)),
                ('data_validade', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(null=True)),
                ('origem', models.CharField(max_length=255, null=True)),
                ('descricao', models.CharField(max_length=255, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, null=True)),
                ('data_validade', models.DateTimeField(null=True)),
            ],
        ),
    ]
