# Generated by Django 2.2.5 on 2019-09-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0002_auto_20190928_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='signin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('pass1', models.TextField()),
                ('pass2', models.TextField()),
            ],
        ),
    ]
