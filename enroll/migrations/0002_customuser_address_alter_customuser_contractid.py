# Generated by Django 5.1 on 2025-01-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='contractId',
            field=models.IntegerField(null=True),
        ),
    ]
