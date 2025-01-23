# Generated by Django 5.1.3 on 2025-01-23 07:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('currency', models.CharField(max_length=100)),
                ('currency_symbol', models.CharField(max_length=10)),
                ('iso_3166_2', models.CharField(max_length=2)),
                ('iso_3166_3', models.CharField(max_length=3)),
                ('calling_code', models.CharField(max_length=10)),
                ('flag', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'CountryModel',
                'verbose_name_plural': 'CountryModels',
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='address.countrymodel')),
            ],
            options={
                'verbose_name': 'StateModel',
                'verbose_name_plural': 'StateModels',
                'db_table': 'State',
            },
        ),
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=20)),
                ('is_default', models.BooleanField(default=False)),
                ('country_code', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='addresses', to=settings.AUTH_USER_MODEL)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='addresses', to='address.countrymodel')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='addresses', to='address.statemodel')),
            ],
            options={
                'verbose_name': 'AddressModel',
                'verbose_name_plural': 'AddressModels',
                'db_table': 'Address',
            },
        ),
    ]
