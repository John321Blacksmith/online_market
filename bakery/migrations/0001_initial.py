# Generated by Django 4.2 on 2023-06-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bread_type', models.CharField(max_length=20)),
                ('weight', models.IntegerField()),
                ('date', models.DateField()),
                ('vendor', models.CharField(max_length=40)),
            ],
        ),
    ]