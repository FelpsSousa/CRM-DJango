# Generated by Django 3.2.8 on 2021-10-25 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20211025_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='norma',
            name='descricao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
