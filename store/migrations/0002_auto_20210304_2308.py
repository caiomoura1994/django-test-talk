# Generated by Django 3.1.7 on 2021-03-05 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='profile',
            new_name='client',
        ),
    ]
