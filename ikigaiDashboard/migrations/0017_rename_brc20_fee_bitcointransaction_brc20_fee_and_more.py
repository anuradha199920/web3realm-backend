# Generated by Django 4.2.2 on 2023-07-11 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikigaiDashboard', '0016_bitcointransaction_alter_volumebyplatform_volume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bitcointransaction',
            old_name='BRC20_Fee',
            new_name='brc20_fee',
        ),
        migrations.RenameField(
            model_name='bitcointransaction',
            old_name='non_BRC20_Ordi_Fee',
            new_name='non_brc20_ordi_fee',
        ),
        migrations.RenameField(
            model_name='bitcointransaction',
            old_name='non_Odrdinal_Fee',
            new_name='non_odrdinal_Fee',
        ),
    ]
