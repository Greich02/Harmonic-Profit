# Generated by Django 3.1.6 on 2021-02-26 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HarmonicProfit', '0004_auto_20210226_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sponsorship_status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.sponsorshipstatus'),
        ),
    ]
