# Generated by Django 2.1.2 on 2018-11-05 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0002_auto_20181105_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='good_photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
    ]
