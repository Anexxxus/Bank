# Generated by Django 3.0.3 on 2022-11-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20221125_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сurrencybase',
            name='Curs_BANK',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='сurrencybase',
            name='Kurs_buy',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='сurrencybase',
            name='Kurs_sell',
            field=models.FloatField(),
        ),
    ]
