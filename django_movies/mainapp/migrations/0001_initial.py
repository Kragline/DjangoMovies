# Generated by Django 4.2.5 on 2023-09-16 10:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("bio", models.TextField(blank=True)),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("photo", models.ImageField(upload_to="actor_photos")),
            ],
            options={
                "verbose_name": "Actor",
                "verbose_name_plural": "Actors",
            },
        ),
        migrations.CreateModel(
            name="Director",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("bio", models.TextField(blank=True)),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("photo", models.ImageField(upload_to="director_photos")),
            ],
            options={
                "verbose_name": "Director",
                "verbose_name_plural": "Directors",
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("description", models.TextField(blank=True)),
                ("slug", models.SlugField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name": "Genre",
                "verbose_name_plural": "Genres",
            },
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("tagline", models.CharField(blank=True, max_length=150)),
                ("about", models.TextField(blank=True)),
                ("year", models.PositiveSmallIntegerField()),
                ("country", models.CharField(max_length=150)),
                ("world_premiere", models.DateField(default=datetime.date.today)),
                ("poster", models.ImageField(upload_to="movie_posters")),
                ("trailer", models.FileField(blank=True, upload_to="movie_trailers")),
                ("rating", models.PositiveSmallIntegerField(blank=True, default=1)),
                (
                    "budget",
                    models.PositiveIntegerField(
                        default=0, help_text="Budget in US dollars"
                    ),
                ),
                ("fees_in_usa", models.PositiveIntegerField(blank=True)),
                ("fees_in_world", models.PositiveIntegerField(default=0)),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                (
                    "actors",
                    models.ManyToManyField(related_name="movies", to="mainapp.actor"),
                ),
                (
                    "directors",
                    models.ManyToManyField(
                        related_name="movies", to="mainapp.director"
                    ),
                ),
                (
                    "genres",
                    models.ManyToManyField(related_name="movies", to="mainapp.genre"),
                ),
            ],
            options={
                "verbose_name": "Movie",
                "verbose_name_plural": "Movies",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="mainapp.movie",
                    ),
                ),
            ],
        ),
    ]
