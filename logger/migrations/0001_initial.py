# Generated by Django 5.2 on 2025-04-20 14:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('user_agent', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('device_type', models.CharField(blank=True, max_length=50)),
                ('device_model', models.CharField(blank=True, max_length=100)),
                ('device_brand', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('redirect_url', models.URLField(blank=True)),
                ('link_id', models.CharField(blank=True, default=uuid.uuid4, max_length=36)),
            ],
        ),
    ]
