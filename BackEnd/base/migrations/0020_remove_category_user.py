# Generated by Django 4.0.6 on 2022-11-19 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_order_createdtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
    ]
