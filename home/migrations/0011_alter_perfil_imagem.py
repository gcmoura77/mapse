# Generated by Django 4.2.9 on 2024-06-29 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_perfil_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
