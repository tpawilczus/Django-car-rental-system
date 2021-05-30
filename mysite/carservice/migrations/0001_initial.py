# Generated by Django 3.1.7 on 2021-05-18 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='photos', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('car_mark', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('car_color', models.CharField(max_length=100)),
                ('num_of_seats', models.IntegerField()),
                ('cost_per_day', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.address')),
            ],
        ),
        migrations.CreateModel(
            name='OrdersArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_score', models.IntegerField(default=0)),
                ('order_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RentalBase',
            fields=[
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='carservice.address')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('number_of_employees', models.IntegerField()),
                ('logo', models.ImageField(upload_to='logo')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.address')),
            ],
        ),
        migrations.CreateModel(
            name='Repairments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine', models.BooleanField(default=False)),
                ('tire', models.BooleanField(default=False)),
                ('door', models.BooleanField(default=False)),
                ('window', models.BooleanField(default=False)),
                ('varnish', models.BooleanField(default=False)),
                ('oil', models.BooleanField(default=False)),
                ('total_price', models.FloatField(blank=True, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.car')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.CharField(max_length=20)),
                ('approved', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('canceled', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('total_price', models.FloatField(blank=True, null=True)),
                ('rate', models.IntegerField(default=0)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.client')),
                ('orders_archive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.ordersarchive')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.seller')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='rental_base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservice.rentalbase'),
        ),
    ]
