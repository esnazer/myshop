# Generated by Django 3.2 on 2022-12-19 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20221219_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cover', to='shop.multimedia'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='thumbs',
            field=models.ManyToManyField(blank=True, null=True, to='shop.Multimedia'),
        ),
    ]
