# Generated by Django 3.0.3 on 2022-11-29 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20221125_2038'),
    ]

    operations = [
        migrations.AlterModelOptions(  # Изменение параметров модели
            name='food',
            options={}, 
        ),
        migrations.CreateModel(  # Создание новой модели
            name='Payment',  # Название новой модели
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Food')),  # Связь с моделью Food
            ],
        ),
    ]
