# Generated by Django 4.1.2 on 2022-10-19 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_rename_artist_artiste_rename_lyrics_lyric_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='data_released',
            new_name='date_released',
        ),
    ]
