# Generated by Django 2.2.17 on 2020-12-09 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TutorialDjango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='', max_length=20000),
        ),
        migrations.AddField(
            model_name='book',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='thumbnail',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='genre',
            name='artist',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='genre',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='genre',
            name='thumbnail',
            field=models.CharField(default='', max_length=500),
        ),
    ]