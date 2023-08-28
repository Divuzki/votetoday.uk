# Generated by Django 4.2.4 on 2023-08-28 15:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField()),
                ('is_ended', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='description',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='election',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='image_link',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='votes',
        ),
        migrations.AddField(
            model_name='candidate',
            name='image_url',
            field=models.URLField(),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Election',
        ),
        migrations.AddField(
            model_name='candidate',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='core.poll'),
            preserve_default=False,
        ),
    ]
