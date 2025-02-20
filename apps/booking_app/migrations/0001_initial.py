# Generated by Django 5.0.7 on 2024-08-07 14:31

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication_app', '0002_alter_customuser_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('train_number', models.CharField(max_length=20, unique=True)),
                ('train_name', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('departure_time', models.TimeField(default=django.utils.timezone.now)),
                ('arrival_time', models.TimeField(default=django.utils.timezone.now)),
                ('total_seats', models.PositiveIntegerField()),
                ('date_from', models.DateField()),
                ('date_upto', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('seat_number', models.IntegerField()),
                ('journey_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customuser', to='authentication_app.customuser')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trains', to='booking_app.train')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
