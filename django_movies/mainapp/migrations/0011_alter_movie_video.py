# Generated by Django 5.0.1 on 2024-01-18 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_movie_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.URLField(default='https://hnembed.cc/embed/movie/imdb_movie_id', max_length=1000),
        ),
    ]
