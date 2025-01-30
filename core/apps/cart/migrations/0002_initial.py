# Generated by Django 5.1.3 on 2025-01-29 13:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmodel',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts', to='product.productmodel'),
        ),
        migrations.AddField(
            model_name='cartmodel',
            name='variation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.variationmodel'),
        ),
        migrations.AddField(
            model_name='couponmodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coupons', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pointsmodel',
            name='consumer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='point', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='wishlistitemmodel',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Wishlist_items', to='product.productmodel'),
        ),
        migrations.AddField(
            model_name='wishlistmodel',
            name='consumer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wishlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='wishlistitemmodel',
            name='wishlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.wishlistmodel'),
        ),
    ]
