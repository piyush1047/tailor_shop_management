# Generated by Django 5.0.4 on 2024-07-30 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0012_order_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='images/'),
        ),
    ]
