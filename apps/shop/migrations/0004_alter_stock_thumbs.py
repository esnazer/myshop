# Generated by Django 3.2 on 2022-12-19 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20221219_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='thumbs',
            field=models.ManyToManyField(blank=True, to='shop.Multimedia'),
        ),
    ]
