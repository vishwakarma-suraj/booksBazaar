# Generated by Django 3.0.6 on 2020-05-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sell', '0007_auto_20200509_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, default='3.png', upload_to='booksBazaar/media'),
        ),
    ]
