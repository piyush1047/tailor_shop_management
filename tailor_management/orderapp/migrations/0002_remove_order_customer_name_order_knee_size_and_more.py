# Generated by Django 5.0.4 on 2024-07-20 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='order',
            name='Knee_Size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='heap',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='heap_loosing',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='langot',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='mohri',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='pant_heap',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='pindli',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='remark',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shirt_length',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shoulder',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='stomach',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='thai',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='garment_type',
            field=models.CharField(choices=[('shirt', 'Shirt'), ('pant', 'Pant'), ('Top-Bottom', 'Top-Bottom')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
