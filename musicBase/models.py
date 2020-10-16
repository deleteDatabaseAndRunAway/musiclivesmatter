from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(null=True)
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


class Song(models.Model):
    song_id = models.IntegerField()
    song_name = models.CharField(max_length=50)
    # song_singer_name = models.CharField(max_length=50)
    song_singer_id = models.IntegerField()
    song_album_id = models.IntegerField()
    song_produce = models.DateTimeField()


class SongComment(models.Model):
    comment_id = models.IntegerField()
    comment_song_id = models.IntegerField()
    comment_msg = models.TextField()


class SongLikes(models.Model):
    like_id = models.IntegerField()
    like_user_id = models.IntegerField()
    like_user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    like_song_id = models.IntegerField()



class Album(models.Model):
    album_id = models.IntegerField()
    album_name = models.CharField(max_length=50)
    album_data = models.DateTimeField()
    album_singer_id = models.IntegerField()


class Singer(models.Model):
    singer_id = models.IntegerField()
    singer_name = models.CharField(max_length=20)
    singer_gender = models.CharField(max_length=10)
    singer_msg = models.TextField()

