from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_gender = models.CharField(max_length=10,null=True)
    user_com = models.CharField(max_length=30,null=True)
    user_birthday = models.DateTimeField(null=True)

    def __str__(self):
        return self.username


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=50)
    album_date = models.DateTimeField(null=True)
    singer_id = models.ForeignKey('Singer',related_name='album_singer', on_delete=models.CASCADE, null=True)

class Singer(models.Model):
    singer_id = models.AutoField(primary_key=True)
    singer_name = models.CharField(max_length=20)
    singer_gender = models.CharField(max_length=10,null=True)
    singer_msg = models.TextField(null=True)


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=50)
    album_id = models.ForeignKey('Album',related_name='song_album', on_delete=models.CASCADE, null=True)
    song_likes = models.IntegerField(null=True, default=0)


class SongComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_song_id = models.ForeignKey('Song',related_name='comment_song', on_delete=models.CASCADE, null=True)
    comment_user_id = models.ForeignKey('User',related_name='comment_user', on_delete=models.CASCADE, null=True)
    comment_msg = models.TextField(null=True)


class SongLikes(models.Model):
    like_id = models.AutoField(primary_key=True)
    like_user_id = models.ForeignKey('User',related_name='like_user', on_delete=models.CASCADE, null=True)
    like_song_id = models.ForeignKey('Song',related_name='like_song', on_delete=models.CASCADE, null=True)


class SongList(models.Model):
    list_id = models.AutoField(primary_key=True)
    list_user_id = models.ForeignKey('User', related_name='list_user', on_delete=models.CASCADE, null=True)
    list_name = models.CharField(max_length=50,null=True)


class CollectInList(models.Model):
    collect_id = models.AutoField(primary_key=True)
    collect_song_id = models.ForeignKey('Song',related_name='collect_song', on_delete=models.CASCADE, null=True)
    collect_list_id = models.ForeignKey('SongList',related_name='collect_list',on_delete=models.CASCADE,null=True)



