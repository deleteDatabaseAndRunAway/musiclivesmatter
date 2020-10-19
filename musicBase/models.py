from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=20,null=True)
    user_gender = models.CharField(max_length=10,null=True)
    user_com_type = models.CharField(max_length=20,null=True)
    user_com = models.CharField(max_length=30,null=True)
    user_birthday = models.DateTimeField(null=True)
    user_show_message = models.BooleanField(null=True)
    user_show_likes = models.BooleanField(null=True)

    def __str__(self):
        return self.user_name

class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=50)
    album_data = models.DateTimeField(null=True)
    album_singer_id = models.IntegerField(null=True)

class Singer(models.Model):
    singer_id = models.AutoField(primary_key=True)
    singer_name = models.CharField(max_length=20)
    singer_gender = models.CharField(max_length=10)
    singer_msg = models.TextField(null=True)


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=50)
    song_singer_id = models.ForeignKey('Singer',related_name='song_singer',on_delete=models.CASCADE)
    song_album_id = models.ForeignKey('Album',related_name='song_album', on_delete=models.CASCADE, null=True)
    song_produce = models.DateTimeField(null=True)


class SongComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_song_id = models.IntegerField(null=True)
    comment_msg = models.ForeignKey('Song',related_name='comment_song', on_delete=models.CASCADE, null=True)


class SongLikes(models.Model):
    like_id = models.AutoField(primary_key=True)
    like_user_id = models.ForeignKey('User',related_name='like_user', on_delete=models.CASCADE, null=True)
    like_song_id = models.ForeignKey('Song',related_name='like_song', on_delete=models.CASCADE, null=True)







