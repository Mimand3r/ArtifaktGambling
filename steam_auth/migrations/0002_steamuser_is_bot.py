# Generated by Django 2.1.2 on 2018-12-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steam_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='steamuser',
            name='is_bot',
            field=models.BooleanField(default=False),
        ),
    ]