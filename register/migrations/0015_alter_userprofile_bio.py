# Generated by Django 3.2.3 on 2021-05-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_alter_userprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]