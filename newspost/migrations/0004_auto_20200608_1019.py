# Generated by Django 3.0.7 on 2020-06-08 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newspost', '0003_auto_20200608_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='articles',
            name='shortdescription',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=250, unique_for_date='publish'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
        migrations.AddField(
            model_name='articles',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='thumbnails/'),
        ),
        migrations.AddField(
            model_name='articles',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
