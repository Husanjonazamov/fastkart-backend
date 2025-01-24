# Generated by Django 5.1.3 on 2025-01-23 18:21

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
            name='CurrencyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='code')),
                ('symbol', models.CharField(max_length=10)),
                ('no_of_decimal', models.IntegerField()),
                ('exchange_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('symbol_position', models.CharField(choices=[('before_price', 'Before'), ('after_price', 'After')], max_length=20)),
                ('thousands_separator', models.CharField(choices=[('comma', 'Comma'), ('dot', 'Dot')], max_length=10)),
                ('decimal_separator', models.CharField(max_length=10)),
                ('system_reserve', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CurrencyModel',
                'verbose_name_plural': 'CurrencyModels',
                'db_table': 'Currency',
            },
        ),
        migrations.CreateModel(
            name='PaymentaccountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paypal_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_holder_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account_no', models.CharField(blank=True, max_length=255, null=True)),
                ('swift', models.CharField(blank=True, max_length=255, null=True)),
                ('ifsc', models.CharField(blank=True, max_length=255, null=True)),
                ('is_default', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PaymentaccountModel',
                'verbose_name_plural': 'PaymentaccountModels',
                'db_table': 'PaymentAccount',
            },
        ),
    ]
