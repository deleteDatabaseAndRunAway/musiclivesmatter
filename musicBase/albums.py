from django.forms import widgets
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django import forms
from musicBase.models import *


class AlbumInfo(forms.Form):
    album_name = forms.CharField(label='专辑名',max_length=50)
    album_data = forms.DateTimeField(label='发行日期')
    album_singer_name = forms.CharField(label='歌手名', max_length=20)


def addAlbum(req):
    if req.method == 'POST':
        af = AlbumInfo(req.POST)
        print(af)
        if af.is_valid():
            # 获得表单数据
            album_singer_name = af.cleaned_data['album_singer_name']
            album_name = af.cleaned_data['album_name']
            album_data = af.cleaned_data['album_data']
            singer = Singer.objects.filter(singer_name=album_singer_name)
            if singer:
                pass;
            else:
                print("nosinger")
                return render(req,'add_album.html', {'af': af,'msg':"请先添加歌手"})
            # 如果有此专辑同样歌手
            albumAndSinger = Album.objects.filter(singer_id=singer[0], album_name=album_name)
            if albumAndSinger:
                return render(req,'add_album.html', {'af': af,'msg':"已有该专辑"})
            else:
                # 添加到数据库
                Album.objects.create(singer_id=singer[0], album_name=album_name, album_date=album_data)
                return render(req,'add_album.html', {'af': af,'msg':"添加专辑成功！"})
        else:
            return render(req,'add_album.html', {'af': af,'msg':"输入信息有格式问题"})
    af = AlbumInfo()
    return render(req,'add_album.html', {'af': af})


def album_delete(req,album_id):
    Album.objects.get(album_id=album_id).delete()
    return redirect("musicBase:album_showall")


def album_index(req:HttpRequest,album_id):
    album = Album.objects.get(album_id=album_id)
    songs = Song.objects.filter(album_id=album)
    return render(req,'albumPage.html',{'songs':songs,'album':album})

#展示
def album_showall(req:HttpRequest):
    albums = Album.objects.select_related().all()
    return render(req,'album_show_all.html',{'albums':albums})
