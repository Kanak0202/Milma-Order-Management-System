# Generated by Django 4.1.4 on 2023-01-25 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mshop', '0002_rename_address_orders_curlocation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilmaCurrentOrder',
            fields=[
                ('current_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default=1)),
                ('name', models.CharField(default='', max_length=50)),
                ('location', models.CharField(default='', max_length=500)),
                ('items_json', models.CharField(default='', max_length=5000)),
                ('orderstatus', models.CharField(max_length=20)),
            ],
        ),
    ]
