# Generated by Django 3.2.7 on 2021-10-17 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
        ('accounts', '0011_auto_20211015_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='saved_resources',
            field=models.ManyToManyField(to='resources.Resource'),
        ),
    ]