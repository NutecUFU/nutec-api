# Generated by Django 2.2.2 on 2019-06-22 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190620_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('first_name',)},
        ),
    ]
