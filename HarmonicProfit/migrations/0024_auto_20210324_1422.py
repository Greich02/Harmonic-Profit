# Generated by Django 3.1.6 on 2021-03-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarmonicProfit', '0023_remove_user_accounttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='earnedFromReferral',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='withdrawableBalance',
            field=models.FloatField(default=0),
        ),
    ]
