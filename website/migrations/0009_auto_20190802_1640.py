# Generated by Django 2.1.4 on 2019-08-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20190802_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=17, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=17, null=True),
        ),
    ]
