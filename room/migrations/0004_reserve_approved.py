# Generated by Django 5.1 on 2025-01-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_reserve_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
