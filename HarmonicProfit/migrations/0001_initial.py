# Generated by Django 3.1.6 on 2021-02-26 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='PromoSpeech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SponsorshipStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('banner', models.CharField(max_length=180)),
                ('description1', models.CharField(max_length=60)),
                ('description2', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=32)),
                ('balance', models.FloatField()),
                ('accountStatus', models.BooleanField()),
                ('referredBby', models.ManyToManyField(related_name='_user_referredBby_+', to='HarmonicProfit.User')),
                ('sponsorship_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.sponsorshipstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('status', models.BooleanField()),
                ('paymentMethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.paymentmethod')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HarmonicProfit.user')),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=60)),
                ('code', models.CharField(max_length=60)),
                ('status', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.user')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('status', models.BooleanField()),
                ('paymentMethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.paymentmethod')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HarmonicProfit.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.user')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.message')),
            ],
        ),
    ]
