# Generated by Django 3.1.4 on 2021-05-19 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0003_auto_20210519_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='reply_count',
            field=models.IntegerField(default=0),
        ),
    ]
