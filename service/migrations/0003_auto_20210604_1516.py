# Generated by Django 3.2.4 on 2021-06-04 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20210604_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='pictureAdd',
        ),
        migrations.AddField(
            model_name='picturework',
            name='work',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='picture_work', to='service.work'),
            preserve_default=False,
        ),
    ]
