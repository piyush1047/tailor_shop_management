# Generated by Django 5.0.4 on 2024-07-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='revenuedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_date', models.CharField(max_length=100, null=True)),
                ('income_category', models.CharField(max_length=100, null=True)),
                ('income_amount', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
