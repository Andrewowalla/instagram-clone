# Generated by Django 4.0.3 on 2022-03-09 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0003_myuser_alter_profile_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='comment',
        ),
    ]