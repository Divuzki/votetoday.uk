# Generated by Django 4.2.4 on 2023-08-28 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_account_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='identifier',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
