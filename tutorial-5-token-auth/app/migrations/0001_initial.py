# Generated by Django 5.1.4 on 2025-01-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('stock_quantity', models.PositiveIntegerField(default=0)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('ratings', models.FloatField(default=0.0)),
            ],
        ),
    ]
