# Generated by Django 4.0.4 on 2023-03-15 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('existence', models.BooleanField(default=True, verbose_name='visiblity')),
                ('order', models.IntegerField(default=True, verbose_name='order')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('named_url', models.CharField(blank=True, max_length=255, verbose_name='named_url')),
                ('url', models.CharField(max_length=255, verbose_name='url')),
            ],
            options={
                'verbose_name': 'menu name',
                'verbose_name_plural': 'menu names',
            },
        ),
        migrations.CreateModel(
            name='MenuEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('existence', models.BooleanField(default=True, verbose_name='visiblity')),
                ('order', models.IntegerField(default=True, verbose_name='order')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('named_url', models.CharField(blank=True, max_length=255, verbose_name='named_url')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menu', verbose_name='menu')),
            ],
            options={
                'verbose_name': 'menu entity',
                'verbose_name_plural': 'menu entities',
            },
        ),
        migrations.CreateModel(
            name='SubMenuEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('existence', models.BooleanField(default=True, verbose_name='visiblity')),
                ('order', models.IntegerField(default=True, verbose_name='order')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('named_url', models.CharField(blank=True, max_length=255, verbose_name='named_url')),
                ('menu_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menuentity')),
            ],
            options={
                'verbose_name': 'sub-menu entity',
                'verbose_name_plural': 'sub-menu entities',
            },
        ),
    ]