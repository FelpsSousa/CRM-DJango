# Generated by Django 3.2.8 on 2021-10-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_aviso_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='norma',
            name='descricao',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
