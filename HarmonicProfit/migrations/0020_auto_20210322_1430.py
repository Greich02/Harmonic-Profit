# Generated by Django 3.1.6 on 2021-03-22 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HarmonicProfit', '0019_auto_20210320_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='message',
        ),
        migrations.DeleteModel(
            name='PromoSpeech',
        ),
        migrations.DeleteModel(
            name='Target',
        ),
        migrations.RemoveField(
            model_name='autopoollist',
            name='autopool1',
        ),
        migrations.RemoveField(
            model_name='autopoollist',
            name='autopool10',
        ),
        migrations.RemoveField(
            model_name='autopoollist',
            name='autopool2',
        ),
        migrations.RemoveField(
            model_name='autopoollist',
            name='autopool3',
        ),
        migrations.RemoveField(
            model_name='autopoollist',
            name='autopool4',
        ),
        migrations.RemoveField(
            model_name='autopoollist',
            name='autopool5',
        ),
        migrations.RemoveField(
            model_name='autopoollist',
            name='autopool6',
        ),
        migrations.RemoveField(
            model_name='autopoollist',
            name='autopool7',
        ),
        migrations.RemoveField(
            model_name='autopoollist',
            name='autopool8',
        ),
        migrations.RemoveField(
            model_name='autopoollist',
            name='autopool9',
        ),
        migrations.RemoveField(
            model_name='withdrawal',
            name='paymentMethod',
        ),
        migrations.AddField(
            model_name='autopoollist',
            name='level',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(default='1', upload_to=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='PaymentMethod',
        ),
    ]
