# Generated by Django 3.2.6 on 2021-08-20 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myname', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]
