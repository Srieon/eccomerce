# Generated by Django 2.2.13 on 2020-08-30 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0002_auto_20200829_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
