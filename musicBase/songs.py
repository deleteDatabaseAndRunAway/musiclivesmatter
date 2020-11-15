from django.forms import widgets
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django import forms
from musicBase import models
from musicBase.models import *
from django.contrib import auth
from django.contrib import messages

class DeleteSongInfo(forms.Form):
    song_name = forms.CharField(label='歌曲名', max_length=100)
    song_album_name = forms.CharField(label='专辑名', max_length=20)

class SongInfo(forms.Form):
    song_name = forms.CharField(label='歌曲名',max_length=100)
    song_album_name = forms.CharField(label='专辑名', max_length=20)


def addSong(req):
    if req.method == 'POST':
        sf = SongInfo(req.POST)
        if sf.is_valid():
            # 获得表单数据
            song_album_name = sf.cleaned_data['song_album_name']
            song_name = sf.cleaned_data['song_name']
            album_foreign = Album.objects.filter(album_name=song_album_name)
            if album_foreign:
                pass;
            else:
                return render(req,'add_song.html', {'sf': sf})
            # 如果有此歌曲同样专辑
            songAndAlbum = Song.objects.filter(album_id=album_foreign[0], song_name=song_name)
            if songAndAlbum:
                return render(req,'add_song.html', {'sf': sf})
            else:
                # 添加到数据库
                Song.objects.create(album_id=album_foreign[0],song_name=song_name,song_likes=0)
                return HttpResponse('add song success!!')
        else:
            print(45)
    sf = SongInfo()
    return render(req,'add_song.html', {'sf': sf})



#展示
def song_showall(req:HttpRequest):
    songs = Song.objects.select_related().all()
    return render(req,'song_showall.html',{'songs':songs})


def song_index(req:HttpRequest,song_id):
    song = Song.objects.filter(song_id=song_id)[0]
    return render(req,'song_index.html',{'song':song})

def like_song(req:HttpRequest,song_id:int):
    if req.user.is_authenticated:
        user = User.objects.get(username=req.user.username)
        song = Song.objects.get(song_id= song_id)
        if SongLikes.objects.filter(like_user_id=user,like_song_id=song):
            return HttpResponse("不能重复喜欢呀")
        SongLikes.objects.create(like_user_id=user,like_song_id=song)
        return HttpResponse("喜欢歌曲成功")
    return HttpResponse("请登录！")
