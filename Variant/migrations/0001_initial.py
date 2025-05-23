# Generated by Django 5.1.4 on 2025-01-12 02:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0003_rename_img_1_productsmodel_img1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariantModel',
            fields=[
                ('variant_id', models.AutoField(primary_key=True, serialize=False)),
                ('img1', models.CharField(max_length=100)),
                ('img2', models.CharField(max_length=100)),
                ('img3', models.CharField(max_length=100)),
                ('video_url', models.CharField(max_length=100)),
                ('retail_price', models.FloatField(max_length=50)),
                ('sell_price', models.FloatField(max_length=50)),
                ('packaging', models.CharField(max_length=50)),
                ('variant_description', models.CharField(max_length=400)),
                ('products_id', models.ForeignKey(db_column='products_id', on_delete=django.db.models.deletion.CASCADE, to='Products.productsmodel')),
            ],
            options={
                'db_table': 'tbl_variant',
            },
        ),
    ]
