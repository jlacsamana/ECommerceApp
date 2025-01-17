# Generated by Django 5.0.6 on 2024-07-10 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageListings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='onAmazon',
            new_name='on_Amazon',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='onEbay',
            new_name='on_Ebay',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='onFBMarketplace',
            new_name='on_FBMarketplace',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='onWooCommerce',
            new_name='on_WooCommerce',
        ),
        migrations.AddField(
            model_name='listing',
            name='additional_description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
