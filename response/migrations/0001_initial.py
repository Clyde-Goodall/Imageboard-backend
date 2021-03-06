# Generated by Django 3.1.4 on 2021-05-19 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('abbrev', models.CharField(max_length=4, unique=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, default='', max_length=500)),
                ('img', models.ImageField(default='none', upload_to='')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='response.board')),
            ],
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, default='', max_length=500)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='response.board')),
                ('thread', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='response.thread')),
            ],
        ),
    ]
