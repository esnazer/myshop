# Generated by Django 3.2 on 2022-12-15 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SuscriptionIU',
        ),
        migrations.DeleteModel(
            name='TokenIU',
        ),
        migrations.RemoveField(
            model_name='user',
            name='business_account',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='user',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='postalcode',
        ),
        migrations.RemoveField(
            model_name='user',
            name='public',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rank_account',
        ),
        migrations.RemoveField(
            model_name='user',
            name='registrado',
        ),
        migrations.RemoveField(
            model_name='user',
            name='stateorprov',
        ),
        migrations.RemoveField(
            model_name='user',
            name='street',
        ),
        migrations.RemoveField(
            model_name='user',
            name='usuario_verificado',
        ),
    ]
