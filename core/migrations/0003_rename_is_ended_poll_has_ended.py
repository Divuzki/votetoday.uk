# Generated by Django 4.2.4 on 2023-08-28 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_poll_remove_candidate_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='is_ended',
            new_name='has_ended',
        ),
    ]
