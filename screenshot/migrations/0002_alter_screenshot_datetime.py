# Generated by Django 4.0.4 on 2022-05-19 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screenshot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
