# Generated by Django 3.0.5 on 2020-04-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20200420_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
