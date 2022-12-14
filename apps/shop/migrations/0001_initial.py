# Generated by Django 3.2 on 2022-12-19 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('description', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Modelo Base',
                'verbose_name_plural': 'Modelos Base',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('file', models.FileField(upload_to='upload/', verbose_name='Archivo')),
                ('type', models.CharField(max_length=5, verbose_name='tipo')),
                ('tag', models.CharField(max_length=150, verbose_name='tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Modelo Base',
                'verbose_name_plural': 'Modelos Base',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('unit', models.CharField(max_length=10)),
                ('brand', models.CharField(max_length=100)),
                ('short_description', models.TextField(max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
            options={
                'verbose_name': 'Modelo Base',
                'verbose_name_plural': 'Modelos Base',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('amount', models.IntegerField(default=0, verbose_name='catidad')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='costo')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'verbose_name': 'Modelo Base',
                'verbose_name_plural': 'Modelos Base',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='precio')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('cover', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cover', to='shop.multimedia')),
                ('store', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.store')),
                ('thumbs', models.ManyToManyField(to='shop.Multimedia')),
            ],
            options={
                'verbose_name': 'Modelo Base',
                'verbose_name_plural': 'Modelos Base',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalStore',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('amount', models.IntegerField(default=0, verbose_name='catidad')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='costo')),
                ('code', models.CharField(db_index=True, max_length=10)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='shop.product')),
            ],
            options={
                'verbose_name': 'historical Modelo Base',
                'verbose_name_plural': 'historical Modelos Base',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalStock',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='precio')),
                ('code', models.CharField(db_index=True, max_length=10)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('cover', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='shop.multimedia')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('store', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='shop.store')),
            ],
            options={
                'verbose_name': 'historical Modelo Base',
                'verbose_name_plural': 'historical Modelos Base',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(db_index=True, max_length=10)),
                ('unit', models.CharField(max_length=10)),
                ('brand', models.CharField(max_length=100)),
                ('short_description', models.TextField(max_length=150)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='shop.category')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Modelo Base',
                'verbose_name_plural': 'historical Modelos Base',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMultimedia',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('file', models.TextField(max_length=100, verbose_name='Archivo')),
                ('type', models.CharField(max_length=5, verbose_name='tipo')),
                ('tag', models.CharField(max_length=150, verbose_name='tag')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Modelo Base',
                'verbose_name_plural': 'historical Modelos Base',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCategory',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=70)),
                ('description', models.TextField(max_length=150)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Modelo Base',
                'verbose_name_plural': 'historical Modelos Base',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
