# Generated by Django 3.0.8 on 2020-07-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_momotranctionid_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='momotranctionid',
            name='transaction_id',
            field=models.CharField(max_length=15),
        ),
    ]
