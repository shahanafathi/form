# Generated by Django 5.0.4 on 2024-04-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regiter',
            name='phonenumber',
            field=models.IntegerField(),
        ),
    ]
