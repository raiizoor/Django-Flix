# Generated by Django 3.2.8 on 2021-10-12 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_alter_video_videos_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='timestamp',
            new_name='created_at',
        ),
    ]
