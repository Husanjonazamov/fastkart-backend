# Generated by Django 5.1.3 on 2025-01-23 13:18

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(unique=True)),
                ('descriptions', models.TextField()),
                ('content', models.TextField()),
                ('meta_title', models.CharField(max_length=100)),
                ('meta_description', models.CharField(max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_sticky', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'BlogModel',
                'verbose_name_plural': 'BlogModels',
                'db_table': 'Blog',
            },
        ),
        migrations.CreateModel(
            name='FaqModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'FaqModel',
                'verbose_name_plural': 'FaqModels',
                'db_table': 'Faq',
            },
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('mime_type', models.CharField(max_length=50)),
                ('disk', models.CharField(default='public', max_length=50)),
                ('size', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('original_url', models.URLField()),
            ],
            options={
                'verbose_name': 'ImageModel',
                'verbose_name_plural': 'ImageModel',
                'db_table': 'Image',
            },
        ),
        migrations.CreateModel(
            name='NotificationdataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('type', models.CharField(choices=[('order', 'Order'), ('payment', 'Payment'), ('refund', 'Refund'), ('coupon', 'Coupon')], max_length=255)),
            ],
            options={
                'verbose_name': 'NotificationdataModel',
                'verbose_name_plural': 'NotificationdataModels',
                'db_table': 'NotificationData',
            },
        ),
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('notifiable_type', models.CharField(max_length=255)),
                ('notifiable_id', models.IntegerField()),
                ('read_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'NotificationModel',
                'verbose_name_plural': 'NotificationModels',
                'db_table': 'Notification',
            },
        ),
        migrations.CreateModel(
            name='QuestionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('reaction', models.CharField(blank=True, max_length=255, null=True)),
                ('total_likes', models.IntegerField(default=0)),
                ('total_dislikes', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'QuestionModel',
                'verbose_name_plural': 'QuestionModels',
                'db_table': 'Question',
            },
        ),
    ]
