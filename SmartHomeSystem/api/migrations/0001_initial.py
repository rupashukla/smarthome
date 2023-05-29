# Generated by Django 4.1.1 on 2022-10-16 11:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('serial_no', models.IntegerField(primary_key=True, serialize=False)),
                ('registered_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=50)),
                ('duration_month', models.IntegerField(blank=True, null=True)),
                ('number_of_devices', models.IntegerField()),
                ('automation_access', models.BooleanField()),
                ('sharable_to', models.IntegerField(default=1)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(4)])),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField(null=True)),
                ('serial_no', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='api.registration')),
                ('subscription_plan_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.subscriptionplan')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('permissions', models.ManyToManyField(to='api.permission')),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.users'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField()),
                ('access_area_id', models.ManyToManyField(to='api.area', verbose_name='Select Areas')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.role')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)])),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)])),
                ('serial_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homeuser', to='api.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField()),
                ('parameters', models.TextField(default={'active': 'off', 'color': 'white', 'speed': None})),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.area')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='home_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.home'),
        ),
    ]
