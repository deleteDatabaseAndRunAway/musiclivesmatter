# Generated by Django 2.1.7 on 2020-10-29 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicBase', '0007_auto_20201029_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='song_produce',
        ),
        migrations.AddField(
            model_name='song',
            name='song_likes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='songcomment',
            name='comment_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to='musicBase.User'),
        ),
        migrations.AlterField(
            model_name='singer',
            name='singer_gender',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='songcomment',
            name='comment_msg',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='songcomment',
            name='comment_song_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_song', to='musicBase.Song'),
        ),
    ]
