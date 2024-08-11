# Generated by Django 5.0.6 on 2024-08-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_banned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='is_banned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='train',
            name='is_banned',
            field=models.BooleanField(default=False),
        ),
    ]
