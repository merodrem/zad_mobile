# Generated by Django 2.1.4 on 2019-07-18 17:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190718_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='flashinfo',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
