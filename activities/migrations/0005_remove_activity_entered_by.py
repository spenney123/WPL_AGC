# Generated by Django 3.0 on 2023-09-06 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20230906_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='entered_by',
        ),
    ]