# Generated by Django 3.2.5 on 2021-07-12 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='transfers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fro_user_id', models.CharField(max_length=50)),
                ('to_user_id', models.CharField(max_length=50)),
                ('amt_transf', models.IntegerField()),
                ('tr_date', models.DateField()),
            ],
        ),
    ]
