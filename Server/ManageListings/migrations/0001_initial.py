# Generated by Django 5.0.6 on 2024-07-08 22:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ManageInventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('onWooCommerce', models.BooleanField(default=False)),
                ('onEbay', models.BooleanField(default=False)),
                ('onAmazon', models.BooleanField(default=False)),
                ('onFBMarketplace', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ManageInventory.inventoryitem')),
            ],
        ),
    ]