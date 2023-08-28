# Generated by Django 4.2.4 on 2023-08-28 16:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_candidate_voters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='voters',
            field=models.ManyToManyField(blank=True, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
