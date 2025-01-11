# Generated by Django 5.1.4 on 2025-01-10 19:36

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_user_age_alter_user_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.CharField(max_length=50, validators=[app.models.validate_name]),
        ),
        migrations.AlterField(
            model_name='user',
            name='lname',
            field=models.CharField(max_length=50, validators=[app.models.validate_name]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=18, validators=[app.models.validate_password]),
        ),
    ]