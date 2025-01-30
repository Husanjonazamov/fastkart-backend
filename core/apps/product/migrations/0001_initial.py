# Generated by Django 5.1.3 on 2025-01-29 13:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('content', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('style', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'AttributeModel',
                'verbose_name_plural': 'AttributeModels',
                'db_table': 'Attribute',
            },
        ),
        migrations.CreateModel(
            name='AttributevalueModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('hex_color', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute_values', to='product.attributemodel')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'AttributevalueModel',
                'verbose_name_plural': 'AttributevalueModels',
                'db_table': 'AttributeValue',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('blog', 'Blog'), ('product', 'Product'), ('both', 'Both'), ('post', 'Post')], max_length=50)),
                ('commission_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('blogs_count', models.IntegerField(default=0)),
                ('products_count', models.IntegerField(default=0)),
                ('category_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_icons', to='content.imagemodel')),
                ('category_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_images', to='content.imagemodel')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='product.categorymodel')),
            ],
            options={
                'verbose_name': 'CategoryModel',
                'verbose_name_plural': 'CategoryModels',
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='CompareModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('consumer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CompareModel',
                'verbose_name_plural': 'CompareModels',
                'db_table': 'Compare',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('short_description', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('simple', 'Simple product'), ('variable', 'Product with variations'), ('grouped', 'Collection of products'), ('external', 'External product'), ('affiliate', 'Affiliate product'), ('virtual', 'Virtual product'), ('downloadable', 'Downloadable product')], max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('shipping_days', models.PositiveIntegerField(blank=True, null=True)),
                ('is_cod', models.BooleanField(default=False)),
                ('is_free_shipping', models.BooleanField(default=False)),
                ('is_sale_enable', models.BooleanField(default=False)),
                ('is_return', models.BooleanField(default=False)),
                ('is_trending', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('sale_starts_at', models.DateTimeField(blank=True, null=True)),
                ('sale_expired_at', models.DateTimeField(blank=True, null=True)),
                ('sku', models.CharField(max_length=255, unique=True)),
                ('is_random_related_products', models.BooleanField(default=False)),
                ('stock_status', models.CharField(choices=[('in_stock', 'In Stock'), ('out_of_stock', 'Out of Stock'), ('on_backorder', 'On Backorder')], default='in_stock', max_length=50)),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('estimated_delivery_text', models.CharField(blank=True, max_length=255, null=True)),
                ('return_policy_text', models.CharField(blank=True, max_length=255, null=True)),
                ('safe_checkout', models.BooleanField(default=False)),
                ('secure_checkout', models.BooleanField(default=False)),
                ('social_share', models.BooleanField(default=False)),
                ('encourage_order', models.BooleanField(default=False)),
                ('encourage_view', models.BooleanField(default=False)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('orders_count', models.PositiveIntegerField(default=0)),
                ('reviews_count', models.PositiveIntegerField(default=0)),
                ('can_review', models.BooleanField(default=True)),
                ('rating_count', models.FloatField(default=0.0)),
                ('order_amount', models.FloatField(default=0.0)),
                ('review_ratings', models.JSONField(blank=True, default=list)),
                ('attributes', models.ManyToManyField(blank=True, related_name='products', to='product.attributemodel')),
                ('categories', models.ManyToManyField(blank=True, related_name='products', to='product.categorymodel')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to=settings.AUTH_USER_MODEL)),
                ('cross_sell_products', models.ManyToManyField(blank=True, related_name='cross_sells', to='product.productmodel')),
                ('product_galleries', models.ManyToManyField(blank=True, related_name='product_galleries', to='content.imagemodel')),
                ('product_meta_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_meta_images', to='content.imagemodel')),
                ('product_thumbnail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_thumbnails', to='content.imagemodel')),
                ('related_products', models.ManyToManyField(blank=True, related_name='related_to_products', to='product.productmodel')),
                ('size_chart_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='size_chart_images', to='content.imagemodel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='CompareitemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('compare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compare_items', to='product.comparemodel')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compare_items', to='product.productmodel')),
            ],
            options={
                'verbose_name': 'CompareitemModel',
                'verbose_name_plural': 'CompareitemModels',
                'db_table': 'CompareItem',
            },
        ),
        migrations.CreateModel(
            name='StoreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('city', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=20)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('pinterest', models.URLField(blank=True, null=True)),
                ('hide_vendor_email', models.BooleanField(default=False)),
                ('hide_vendor_phone', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('orders_count', models.IntegerField(default=0)),
                ('reviews_count', models.IntegerField(default=0)),
                ('products_count', models.IntegerField(default=0)),
                ('order_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('rating_count', models.IntegerField(default=0)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stores', to='address.countrymodel')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stores_created', to=settings.AUTH_USER_MODEL)),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stores', to='address.statemodel')),
                ('store_cover', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='store_covers', to='content.imagemodel')),
                ('store_logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='store_logos', to='content.imagemodel')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stores', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'StoreModel',
                'verbose_name_plural': 'StoreModels',
                'db_table': 'Store',
            },
        ),
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('consumer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='product.productmodel')),
                ('review_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.imagemodel')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='product.storemodel')),
            ],
            options={
                'verbose_name': 'ReviewModel',
                'verbose_name_plural': 'ReviewModels',
                'db_table': 'Review',
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.storemodel'),
        ),
        migrations.CreateModel(
            name='TagsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('blog', 'Blog'), ('post', 'Post'), ('product', 'Product'), ('category', 'Category'), ('brand', 'Brand'), ('size', 'Size'), ('color', 'Color')], max_length=100)),
                ('descriptions', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('blogs_count', models.IntegerField(default=0)),
                ('products_count', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'TagsModel',
                'verbose_name_plural': 'TagsModels',
                'db_table': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='products', to='product.tagsmodel'),
        ),
        migrations.CreateModel(
            name='TaxModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taxes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'TaxModel',
                'verbose_name_plural': 'TaxModels',
                'db_table': 'Tax',
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.taxmodel'),
        ),
        migrations.CreateModel(
            name='VariationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('stock_status', models.CharField(choices=[('in_stock', 'In Stock'), ('out_of_stock', 'Out of Stock'), ('on_backorder', 'On Backorder')], max_length=50)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sku', models.CharField(max_length=50)),
                ('status', models.IntegerField()),
                ('variation_options', models.JSONField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attribute_values', models.ManyToManyField(related_name='variations', to='product.attributevaluemodel')),
                ('variation_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.imagemodel')),
            ],
            options={
                'verbose_name': 'Variation Model',
                'verbose_name_plural': 'Variation Models',
                'db_table': 'Variation ',
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='variations',
            field=models.ManyToManyField(blank=True, related_name='products', to='product.variationmodel'),
        ),
    ]
