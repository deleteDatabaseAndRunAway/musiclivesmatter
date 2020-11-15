from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django import forms
from musicBase import models
from musicBase.models import *

from django.views.decorators.csrf import csrf_exempt

class SongInfo(forms.Form):
    song_name = forms.CharField(label='歌名', max_length=50)
    song_singer_name = forms.CharField(label='歌手名', max_length=20)


class SingerInfo(forms.Form):
    singer_name = forms.CharField(label='歌手名', max_length=20)
    singer_gender = forms.CharField(label='性别', max_length=10)
    singer_msg = forms.TextInput()


class AlbumInfo(forms.Form):
    album_name = forms.CharField(max_length=50)
    album_data = forms.DateTimeField()
    album_singer_name = forms.CharField(label='歌手名', max_length=20)
# 注册


class Like(forms.Form):
    like_song_name = forms.CharField(max_length=50)


# 登陆成功
def index(req:HttpRequest):
    print(req.user.is_authenticated)
    return render(req,'index.html')

def showUser(req):
    userlist = models.User.objects.all()
    return render(req,'showUser.html', {'userlist':userlist})


def showLike(req):
    user_name = req.COOKIES['username']
    user_id = User.objects.filter(user_name=user_name)
    likelist = SongLikes.objects.filter(like_user_id=user_id)
    return render(req, 'showLike.html', {'likelist': likelist})


def showOtherLike(req):
    if req.method == 'POST':
        user_name = req.POST['user_name']
        user_id = User.objects.filter(user_name=user_name)
        likelist = SongLikes.objects.filter(like_user_id=user_id)
        return render(req, 'showLike.html', {'likelist': likelist})


def showSimilarity(req):
    if req.method == 'POST':
        user_name = req.POST['user_name']
        user_id = User.objects.filter(user_name=user_name)
        likelist1 = SongLikes.objects.filter(like_user_id=user_id)
        user_name = req.COOKIES['username']
        user_id = User.objects.filter(user_name=user_name)
        likelist2 = SongLikes.objects.filter(like_user_id=user_id)
        return HttpResponse("the similarity between your likeSong and the selected user's is xxx")


def addComment(req):
    if req.method == 'POST':
        # user_name = req.COOKIES['username']
        # user_id = User.objects.filter(user_name=user_name)
        song_name = req.POST['song_name']
        comment_msg = req.POST['comment']
        comment_song_id = Song.objects.filter(song_name=song_name).id
        SongLikes.objects.create(comment_song_id=comment_song_id, comment_msg=comment_msg)
        return HttpResponse("comment success")


def music_manage(req:HttpRequest):
    render(req,'musicMange.html')
