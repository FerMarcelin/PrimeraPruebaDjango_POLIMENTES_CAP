# Generated by Django 3.1 on 2021-08-17 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(blank=True, max_length=64),
        ),
    ]
