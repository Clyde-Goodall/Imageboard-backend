# Generated by Django 3.1.4 on 2021-05-19 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0002_auto_20210518_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replies',
            name='board',
        ),
        migrations.AlterField(
            model_name='replies',
            name='content',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='replies',
            name='thread',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='response.thread'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='board',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='response.board'),
        ),
    ]