# Generated by Django 4.0.4 on 2022-05-22 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='messages',
            new_name='message',
        ),
    ]
