# Generated by Django 3.1.7 on 2021-05-20 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carservice', '0006_auto_20210520_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orders_archive',
        ),
        migrations.AddField(
            model_name='ordersarchive',
            name='order',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='carservice.order'),
        ),
    ]