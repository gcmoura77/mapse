# Generated by Django 4.2.9 on 2024-07-18 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0022_alter_questionarioempresa_data_ativacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='login_mapeamento',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
