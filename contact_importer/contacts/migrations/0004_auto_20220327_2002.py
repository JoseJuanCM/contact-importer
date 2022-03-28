# Generated by Django 3.2.12 on 2022-03-28 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20220327_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='last4',
            field=models.CharField(default='', max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='card',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='franchise',
            field=models.CharField(max_length=50),
        ),
    ]
