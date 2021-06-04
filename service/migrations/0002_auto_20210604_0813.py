# Generated by Django 3.2.4 on 2021-06-04 08:13

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='document',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AddField(
            model_name='work',
            name='video',
            field=models.URLField(blank=True),
        ),
    ]