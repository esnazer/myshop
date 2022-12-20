# Generated by Django 3.2 on 2022-12-19 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='historicalcategory',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Category', 'verbose_name_plural': 'historical Categories'},
        ),
        migrations.AlterModelOptions(
            name='historicalmultimedia',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Multimedia', 'verbose_name_plural': 'historical Multimedias'},
        ),
        migrations.AlterModelOptions(
            name='historicalproduct',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Product', 'verbose_name_plural': 'historical Products'},
        ),
        migrations.AlterModelOptions(
            name='historicalstock',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Stock', 'verbose_name_plural': 'historical Stock'},
        ),
        migrations.AlterModelOptions(
            name='historicalstore',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Store', 'verbose_name_plural': 'historical Store'},
        ),
        migrations.AlterModelOptions(
            name='multimedia',
            options={'verbose_name': 'Multimedia', 'verbose_name_plural': 'Multimedias'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Stock', 'verbose_name_plural': 'Stock'},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name': 'Store', 'verbose_name_plural': 'Store'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='historicalcategory',
            name='slug',
            field=models.SlugField(editable=False, max_length=70),
        ),
    ]
