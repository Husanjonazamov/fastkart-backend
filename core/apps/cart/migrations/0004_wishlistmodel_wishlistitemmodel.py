# Generated by Django 5.1.3 on 2025-01-22 18:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_pointsmodel'),
        ('product', '0005_reviewmodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('consumer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wishlist', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'WishlistModel',
                'verbose_name_plural': 'WishlistModels',
                'db_table': 'Wishlist',
            },
        ),
        migrations.CreateModel(
            name='WishlistitemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Wishlist_items', to='product.productmodel')),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.wishlistmodel')),
            ],
            options={
                'verbose_name': 'WishlistitemModel',
                'verbose_name_plural': 'WishlistitemModels',
                'db_table': 'WishlistItem',
            },
        ),
    ]
