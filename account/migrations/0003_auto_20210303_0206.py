# Generated by Django 3.1.7 on 2021-03-02 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210303_0146'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='developer',
            new_name='user',
        ),
    ]
