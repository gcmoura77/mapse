# Generated by Django 4.2.9 on 2024-06-27 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_email_empresa_email_contato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='cnpj',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
    ]
