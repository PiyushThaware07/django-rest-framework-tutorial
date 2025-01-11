# Generated by Django 5.1.4 on 2025-01-11 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_author_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='books', to='app.tag'),
        ),
    ]