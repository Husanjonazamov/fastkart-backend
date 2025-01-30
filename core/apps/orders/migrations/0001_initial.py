# Generated by Django 5.1.3 on 2025-01-29 13:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('cart', '0002_initial'),
        ('content', '0002_initial'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderstatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('sequence', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('system_reserve', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'OrderstatusModel',
                'verbose_name_plural': 'OrderstatusModels',
                'db_table': 'OrderStatus',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(blank=True, null=True, unique=True)),
                ('tax_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('shipping_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('points_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('wallet_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coupon_total_discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('payment_method', models.CharField(choices=[('paypal', 'Paypal'), ('stripe', 'Stripe'), ('razorpay', 'Razorpay'), ('cod', 'Cod'), ('wallet', 'Wallet'), ('points', 'Points')], max_length=50)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('refunded', 'Refunded'), ('cancelled', 'Cancelled'), ('failed', 'Failed'), ('partially_refunded', 'Partially Refunded')], max_length=50)),
                ('delivery_description', models.CharField(max_length=255)),
                ('delivery_interval', models.CharField(blank=True, max_length=255, null=True)),
                ('invoice_url', models.URLField(blank=True)),
                ('status', models.BooleanField(default=True)),
                ('delivered_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_billings', to='address.addressmodel')),
                ('consumer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='cart.couponmodel')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_orders', to='orders.ordermodel')),
                ('products', models.ManyToManyField(to='product.productmodel')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_shippings', to='address.addressmodel')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='product.storemodel')),
                ('order_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orderstatusmodel')),
            ],
            options={
                'verbose_name': 'OrderModel',
                'verbose_name_plural': 'OrderModels',
                'db_table': 'Order',
            },
        ),
        migrations.CreateModel(
            name='RefundModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('payment_type', models.CharField(choices=[('cash', 'Cash'), ('bank', 'Bank'), ('paypal', 'Paypal'), ('stripe', 'Stripe'), ('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('mobile_money', 'Mobile Money'), ('other', 'Other')], max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('refunded', 'Refunded'), ('cancelled', 'Cancelled'), ('failed', 'Failed'), ('partially_refunded', 'Partially Refunded')], max_length=50)),
                ('is_used', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('consumer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.ordermodel')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.productmodel')),
                ('refund_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.imagemodel')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.storemodel')),
                ('variation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.variationmodel')),
            ],
            options={
                'verbose_name': 'RefundModel',
                'verbose_name_plural': 'RefundModels',
                'db_table': 'Refund',
            },
        ),
    ]
