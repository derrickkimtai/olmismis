# Generated by Django 3.2.12 on 2024-06-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20240604_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='is_number',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='id_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
