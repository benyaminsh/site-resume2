# Generated by Django 4.0 on 2022-01-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_settings_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='تصویر شما '),
        ),
    ]