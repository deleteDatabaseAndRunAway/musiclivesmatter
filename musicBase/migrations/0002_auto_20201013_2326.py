# Generated by Django 2.1.7 on 2020-10-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicBase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_id', models.IntegerField()),
                ('album_name', models.CharField(max_length=50)),
                ('album_data', models.DateTimeField()),
                ('album_singer_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_id', models.IntegerField()),
                ('song_name', models.CharField(max_length=50)),
                ('song_singer_id', models.IntegerField()),
                ('song_album_id', models.IntegerField()),
                ('song_produce', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SongComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.IntegerField()),
                ('comment_song_id', models.IntegerField()),
                ('comment_msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SongLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_id', models.IntegerField()),
                ('like_user_id', models.IntegerField()),
                ('like_song_id', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='user_birthday',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_com',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_com_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_show_likes',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_show_message',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
