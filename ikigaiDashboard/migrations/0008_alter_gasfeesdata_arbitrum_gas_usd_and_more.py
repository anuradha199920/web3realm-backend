# Generated by Django 4.2.2 on 2023-07-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikigaiDashboard', '0007_ethereumwallets_gasfeesdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasfeesdata',
            name='arbitrum_gas_usd',
            field=models.DecimalField(decimal_places=9, max_digits=12),
        ),
        migrations.AlterField(
            model_name='gasfeesdata',
            name='ethereum_gas_usd',
            field=models.DecimalField(decimal_places=9, max_digits=12),
        ),
        migrations.AlterField(
            model_name='gasfeesdata',
            name='optimism_gas_usd',
            field=models.DecimalField(decimal_places=9, max_digits=12),
        ),
        migrations.AlterField(
            model_name='gasfeesdata',
            name='polygon_gas_usd',
            field=models.DecimalField(decimal_places=9, max_digits=12),
        ),
    ]
