# Generated by Django 3.0.6 on 2020-05-09 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sell', '0002_auto_20200509_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
