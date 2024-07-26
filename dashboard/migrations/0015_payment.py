# Generated by Django 3.2.12 on 2024-07-25 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_farmer_agreement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('church', models.CharField(max_length=1, null=True)),
                ('berry_type', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_received', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_per_kilo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.farmer')),
                ('harvest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.harvest')),
            ],
        ),
    ]
