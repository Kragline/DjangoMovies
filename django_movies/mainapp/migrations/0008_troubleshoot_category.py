# Generated by Django 4.2.6 on 2023-10-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_troubleshoot'),
    ]

    operations = [
        migrations.AddField(
            model_name='troubleshoot',
            name='category',
            field=models.CharField(choices=[('page_load_error', 'The page does not load'), ('quality_error', 'Movie quality is bad'), ('account_error', "Can't change account information"), ('no_error_category', 'Other')], default='no_error_category', max_length=150),
        ),
    ]
