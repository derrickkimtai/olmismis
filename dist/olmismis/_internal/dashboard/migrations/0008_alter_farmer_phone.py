# Generated by Django 3.2.12 on 2024-06-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20240604_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='phone',
            field=models.CharField(max_length=18),
        ),
    ]
