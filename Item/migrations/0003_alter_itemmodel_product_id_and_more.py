# Generated by Django 5.1.4 on 2025-02-24 23:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0002_itemmodel_price_itemmodel_qty_and_more'),
        ('Products', '0003_rename_img_1_productsmodel_img1_and_more'),
        ('Variant', '0002_remove_variantmodel_products_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.productsmodel'),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='variant_id',
            field=models.ForeignKey(db_column='variant_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Variant.variantmodel'),
        ),
    ]
