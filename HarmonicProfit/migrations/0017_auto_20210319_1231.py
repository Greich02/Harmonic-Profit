# Generated by Django 3.1.6 on 2021-03-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarmonicProfit', '0016_auto_20210319_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='changeGender',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='removeUsername',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='useLastNameFirstName',
            field=models.BooleanField(default=0),
        ),
    ]
