# Generated by Django 3.2 on 2022-11-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20221109_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pairing',
            name='food',
        ),
        migrations.AddField(
            model_name='food',
            name='pairing',
            field=models.ManyToManyField(to='products.Pairing'),
        ),
    ]
