# Generated by Django 2.2.5 on 2019-11-22 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0014_cropregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropregistration',
            name='area',
            field=models.CharField(max_length=50),
        ),
    ]
