# Generated by Django 3.2.3 on 2021-06-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0026_rename_contactform_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=120),
        ),
    ]