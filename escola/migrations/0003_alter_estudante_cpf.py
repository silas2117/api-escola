# Generated by Django 5.1 on 2024-08-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudante',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
