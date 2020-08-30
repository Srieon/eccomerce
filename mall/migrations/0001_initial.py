# Generated by Django 2.2.13 on 2020-08-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_des', models.CharField(max_length=200)),
                ('product_date', models.DateField()),
            ],
        ),
    ]
