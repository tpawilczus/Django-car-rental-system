# Generated by Django 3.1.7 on 2021-05-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carservice', '0002_auto_20210519_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='car',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='car',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
