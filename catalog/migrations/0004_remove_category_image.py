# Generated by Django 3.0 on 2020-06-30 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200630_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]