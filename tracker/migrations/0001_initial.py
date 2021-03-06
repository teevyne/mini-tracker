# Generated by Django 3.2.6 on 2021-08-25 12:07

from django.db import migrations, models
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cylinder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cylinder_number', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('assigned_on', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', django_fsm.FSMField(choices=[('with-retailer', 'with-retailer'), ('with-dispatch', 'with-dispatch'), ('with-user', 'with-user')], default='with-retailer', max_length=50, protected=True)),
            ],
        ),
    ]
