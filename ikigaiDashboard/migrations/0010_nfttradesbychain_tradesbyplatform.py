# Generated by Django 4.2.2 on 2023-07-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikigaiDashboard', '0009_nftlowestsaleprices'),
    ]

    operations = [
        migrations.CreateModel(
            name='NftTradesByChain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('chain', models.CharField(max_length=50)),
                ('number_of_trades', models.IntegerField()),
            ],
            options={
                'db_table': 'nfttradesbychain',
            },
        ),
        migrations.CreateModel(
            name='TradesByPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('platform', models.CharField(max_length=100)),
                ('unique_traders', models.IntegerField()),
            ],
            options={
                'db_table': 'tradesbyplatform',
            },
        ),
    ]