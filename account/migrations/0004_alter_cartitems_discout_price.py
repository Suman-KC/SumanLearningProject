# Generated by Django 4.2.1 on 2023-06-27 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_cartitems_discout_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='discout_price',
            field=models.FloatField(null=True),
        ),
    ]
