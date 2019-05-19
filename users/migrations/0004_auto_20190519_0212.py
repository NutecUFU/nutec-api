# Generated by Django 2.1.7 on 2019-05-19 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='lattes',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linked',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default='http://nutec.ufu.br/assets/images/group/user.png', upload_to='uploads'),
        ),
    ]
