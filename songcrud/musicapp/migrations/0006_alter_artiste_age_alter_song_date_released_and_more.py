# Generated by Django 4.1.2 on 2022-10-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0005_alter_song_date_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiste',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
