# Generated by Django 4.2.5 on 2023-09-29 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_saga_movie_saga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='saga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='mainapp.saga'),
        ),
    ]
