# Generated by Django 5.1.3 on 2025-01-28 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_rename_user_paymentaccountmodel_consumer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentaccountmodel',
            old_name='consumer',
            new_name='user',
        ),
    ]
