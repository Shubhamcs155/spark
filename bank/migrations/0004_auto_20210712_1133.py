# Generated by Django 3.2.5 on 2021-07-12 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_rename_transfers_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='tr_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='tr_date',
            field=models.DateField(auto_now=True),
        ),
    ]