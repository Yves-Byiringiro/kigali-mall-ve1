# Generated by Django 3.0.8 on 2020-07-26 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200726_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='shipping_price',
            field=models.DecimalField(decimal_places=2, default=2.0, max_digits=7),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
