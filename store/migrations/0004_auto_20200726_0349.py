# Generated by Django 3.0.8 on 2020-07-26 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='customer',
            new_name='user',
        ),
    ]
