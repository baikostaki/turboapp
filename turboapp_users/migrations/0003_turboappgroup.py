# Generated by Django 5.0.6 on 2024-06-09 15:59

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('turboapp_users', '0002_alter_turboappuser_managers_turboappuser_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurboappGroup',
            fields=[
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]