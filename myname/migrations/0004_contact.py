# Generated by Django 3.2.6 on 2021-08-20 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myname', '0003_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
