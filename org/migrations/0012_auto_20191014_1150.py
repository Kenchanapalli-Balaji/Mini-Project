# Generated by Django 2.2.5 on 2019-10-14 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0011_auto_20191014_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineerregister',
            name='LastName',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='farmerregistration',
            name='mailid',
            field=models.EmailField(max_length=254),
        ),
    ]
