# Generated by Django 3.1.7 on 2021-03-02 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210303_0206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='handle',
        ),
    ]