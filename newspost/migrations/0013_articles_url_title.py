# Generated by Django 3.0.7 on 2020-06-11 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspost', '0012_video_exclusivevideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='url_title',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
