# Generated by Django 3.2.25 on 2024-06-26 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fred', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['created_date']},
        ),
    ]
