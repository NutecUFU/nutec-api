# Generated by Django 2.1.7 on 2019-05-13 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20190513_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
    ]
