# Generated by Django 2.0.13 on 2021-02-06 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
