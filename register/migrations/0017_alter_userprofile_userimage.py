# Generated by Django 3.2.3 on 2021-05-31 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_alter_userprofile_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userImage',
            field=models.ImageField(blank=True, default='media/images/default_profile.jpg', null=True, upload_to='images/'),
        ),
    ]
