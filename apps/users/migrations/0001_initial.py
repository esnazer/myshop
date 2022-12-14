# Generated by Django 3.2 on 2022-12-15 04:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electronico')),
                ('nombres', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombres')),
                ('apellidos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellidos')),
                ('country', models.CharField(blank=True, choices=[('CU', 'Cuba'), ('US', 'USA'), ('ES', 'Spain'), ('GB', 'United Kingdom')], max_length=2, null=True)),
                ('postalcode', models.IntegerField(blank=True, null=True)),
                ('organization', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('stateorprov', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen', models.ImageField(blank=True, max_length=200, null=True, upload_to='perfil/', verbose_name='Imagen de Perfil')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administrador', models.BooleanField(default=False)),
                ('usuario_verificado', models.BooleanField(blank=True, default=False, null=True)),
                ('registrado', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Registrado')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Ultima Modificaci??n')),
                ('deleted_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de Eliminaci??n')),
                ('public', models.BooleanField(blank=True, default=False, null=True)),
                ('business_account', models.BooleanField(blank=True, default=False, null=True)),
                ('rank_account', models.IntegerField(blank=True, choices=[(0, 'Usuarios basicos'), (10, 'Usuarios con cuenta Business'), (20, 'Usuarios Promotor'), (30, 'Administracion y Soporte')], default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SuscriptionIU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('seccion', models.CharField(blank=True, max_length=100, null=True)),
                ('categoria', models.CharField(blank=True, max_length=100, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Ultima Modificaci??n')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-create_date',),
            },
        ),
        migrations.CreateModel(
            name='TokenIU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=255)),
                ('uso', models.CharField(choices=[('register', 'Registro de Cuenta'), ('reset', 'Resetear Contrase??a'), ('support', 'Verificaci??n de Soporte'), ('tike', 'Tike de Reporte')], max_length=15)),
                ('valid_from', models.DateTimeField(auto_now_add=True)),
                ('valid_to', models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 18, 4, 12, 48, 496518, tzinfo=utc), null=True)),
                ('usuario', models.CharField(blank=True, max_length=254, null=True)),
                ('activado', models.BooleanField(blank=True, default=False, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creado')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Ultima Modificaci??n')),
            ],
            options={
                'ordering': ('-valid_from',),
            },
        ),
    ]
