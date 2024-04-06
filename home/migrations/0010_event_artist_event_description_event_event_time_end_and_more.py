# Generated by Django 5.0.2 on 2024-04-05 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_eventcustomerref'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='artist',
            field=models.CharField(default='Taylor Swift', max_length=50),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='NA'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_time_end',
            field=models.TimeField(default='18:19:31'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_time_start',
            field=models.TimeField(default='18:19:31'),
        ),
    ]