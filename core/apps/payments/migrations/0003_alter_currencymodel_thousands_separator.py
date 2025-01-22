# Generated by Django 5.1.3 on 2025-01-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_currencymodel_thousands_separator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencymodel',
            name='thousands_separator',
            field=models.CharField(choices=[('comma', 'Comma'), ('dot', 'Dot')], max_length=10),
        ),
    ]
