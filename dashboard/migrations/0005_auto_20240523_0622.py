# Generated by Django 3.2.12 on 2024-05-23 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20240522_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer',
            name='coffe_weight',
        ),
        migrations.AlterField(
            model_name='farmer',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]