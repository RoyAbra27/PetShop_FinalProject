# Generated by Django 4.0.6 on 2022-08-07 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_cart_amount_cart_total_price_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='shelly',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
