# Generated by Django 3.2.6 on 2021-08-25 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cylinder',
            name='assigned_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cylinder',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
