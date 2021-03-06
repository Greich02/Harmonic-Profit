# Generated by Django 3.1.6 on 2021-03-19 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HarmonicProfit', '0012_auto_20210318_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autopool1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivedInvestment', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.user')),
            ],
        ),
        migrations.CreateModel(
            name='Autopool10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivedInvestment', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.user')),
            ],
        ),
        migrations.CreateModel(
            name='Autopool2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivedInvestment', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.user')),
            ],
        ),
        migrations.CreateModel(
            name='Autopool3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivedInvestment', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.user')),
            ],
        ),
        migrations.CreateModel(
            name='Autopool4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivedInvestment', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.user')),
            ],
        ),
        migrations.CreateModel(
            name='Autopool5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivedInvestment', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.user')),
            ],
        ),
        migrations.CreateModel(
            name='Autopool6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivedInvestment', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.user')),
            ],
        ),
        migrations.CreateModel(
            name='Autopool7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivedInvestment', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.user')),
            ],
        ),
        migrations.CreateModel(
            name='Autopool8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivedInvestment', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.user')),
            ],
        ),
        migrations.CreateModel(
            name='Autopool9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receivedInvestment', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.user')),
            ],
        ),
        migrations.CreateModel(
            name='AutopoolList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField()),
                ('autopool1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.autopool1')),
                ('autopool10', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.autopool10')),
                ('autopool2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.autopool2')),
                ('autopool3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.autopool3')),
                ('autopool4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.autopool4')),
                ('autopool5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.autopool5')),
                ('autopool6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.autopool6')),
                ('autopool7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.autopool7')),
                ('autopool8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.autopool8')),
                ('autopool9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HarmonicProfit.autopool9')),
            ],
        ),
    ]
