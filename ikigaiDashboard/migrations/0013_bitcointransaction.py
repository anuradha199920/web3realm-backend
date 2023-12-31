# Generated by Django 4.2.2 on 2023-07-11 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikigaiDashboard', '0012_delete_bitcointransaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='BitcoinTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('non_odrdinal_tx', models.IntegerField()),
                ('brc20_tx', models.IntegerField()),
                ('non_brc20_ordi_tx', models.IntegerField()),
                ('non_odrdinal_fee', models.DecimalField(decimal_places=8, max_digits=10)),
                ('brc20_fee', models.DecimalField(decimal_places=8, max_digits=10)),
                ('non_brc20_ordi_fee', models.DecimalField(decimal_places=8, max_digits=10)),
            ],
            options={
                'db_table': 'bitcointransaction',
            },
        ),
    ]
