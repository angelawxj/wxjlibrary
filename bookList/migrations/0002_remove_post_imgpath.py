# Generated by Django 2.0.5 on 2018-05-28 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookList', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imgpath',
        ),
    ]