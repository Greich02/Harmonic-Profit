# Generated by Django 3.1.6 on 2021-03-31 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarmonicProfit', '0025_auto_20210330_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('token', models.CharField(max_length=35)),
                ('status', models.BooleanField(default=1)),
            ],
        ),
    ]
