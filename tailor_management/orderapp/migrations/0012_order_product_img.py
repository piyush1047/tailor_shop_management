# Generated by Django 5.0.4 on 2024-07-30 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0011_alter_order_deliver_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='orders/'),
        ),
    ]
