# Generated by Django 3.2 on 2022-10-07 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20221007_1128'),
        ('products', '0006_auto_20220924_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='category',
        ),
        migrations.RemoveField(
            model_name='food',
            name='product_type',
        ),
        migrations.RemoveField(
            model_name='food',
            name='slug',
        ),
        migrations.DeleteModel(
            name='ExperienceType',
        ),
        migrations.DeleteModel(
            name='Wine',
        ),
    ]
