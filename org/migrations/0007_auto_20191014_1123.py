# Generated by Django 2.2.5 on 2019-10-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0006_auto_20191014_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerregistration',
            name='emailid',
            field=models.EmailField(default='k@gmail.com', max_length=254),
        ),
    ]