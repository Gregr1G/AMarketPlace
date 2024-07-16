# Generated by Django 5.0.7 on 2024-07-16 01:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        ('market', '0003_remove_product_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='Users.shop'),
            preserve_default=False,
        ),
    ]
