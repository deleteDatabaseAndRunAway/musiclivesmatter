from django.forms import widgets
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django import forms
from musicBase.models import *

class DeleteAlbumInfo(forms.Form):
    album_name = forms.CharField(label='专辑名', max_length=100)

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
                return render(req,'add_album.html', {'af': af})
            # 如果有此专辑同样歌手
            albumAndSinger = Album.objects.filter(album_singer_id=singer[0], album_name=album_name)
            if albumAndSinger:
                return render(req,'add_album.html', {'af': af})
            else:
                # 添加到数据库
                Album.objects.create(album_singer_id=singer[0], album_name=album_name, album_date=album_data)
                return HttpResponse('add success!!')
        else:
            print(45)
    af = AlbumInfo()
    return render(req,'add_album.html', {'af': af})


def delete_album(req):
    if req.method == 'POST':
        uf = DeleteAlbumInfo(req.POST)
        if uf.is_valid():
            cleaned = uf.clean()
            album_to_delete = Album.objects.filter(album_name_exact=cleaned['album_name'])
            if album_to_delete:
                album_to_delete.delete()
                return HttpResponse('add album success!!')
            return HttpResponse('no album Singer!')
    else:
        uf = DeleteAlbumInfo()
    return render(req,'delete_album.html', {'uf': uf})

#展示
def album_showall(req:HttpRequest):
    albums = Album.objects.select_related().all()
    return render(req,'album_show_all.html',{'albums':albums})
