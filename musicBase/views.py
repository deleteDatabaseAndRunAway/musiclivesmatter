from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from musicBase import models
from musicBase.models import *
from django.views.decorators.csrf import csrf_exempt


# 表单
class UserInfo(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', max_length= 100)


class UserRegistInfo(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', max_length=100)
    repeat_password = forms.CharField(label='确认密码', max_length=100)


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


def regist(req):
    if (req.method == 'POST') | (req.method == 'GET'):
        print("req : %s\n" % req)
        uf = UserRegistInfo(req.POST)
        print("uf : %s\n" % uf)
        print(uf._errors)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            repeat_password = uf.cleaned_data['repeat_password']
            user = User.objects.filter(user_name__exact=username)
            print("35\n")
            if user:
                if password != repeat_password:
                    print(uf.password)
                    print(uf.repeat_password)
                    return render_to_response('user_Register.html', {'uf': uf})
            User.objects.create(user_name=username, password=password)
            return HttpResponse('regist success!!')
        else:
            print(45)
    else:
        print(req.method)
        uf = UserInfo()
    return render_to_response('user_Register.html', {'uf': uf})


def delet_user(req):
    if req.method == 'POST':
        uf = UserInfo(req.POST)
        if uf.is_valid():

            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            # 与数据库比较
            user = User.objects.filter(user_name__exact=username, password__exact=password)
            if user:

                # 比较成功删除
                response = HttpResponseRedirect('/musicBase')
                return response
            return HttpResponse('no such User!')
    else:
        uf = UserInfo()
    return HttpResponse('type error!')
    # return render_to_response('register.html', {'uf': uf}, context_instance=RequestContext(req))


# 登陆
def login(req):
    if req.method == 'POST':
        uf = UserInfo(req.POST)
        if uf.is_valid():

            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            # 获取的表单数据与数据库进行比较
            user = User.objects.filter(user_name__exact=username, password__exact=password)
            if user:

                # 比较成功，跳转index
                response = HttpResponseRedirect('/musicBase/index/')

                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3600)
                return response
            else:

                # 比较失败，还在login
                return HttpResponseRedirect('/musicBase/login/')
    else:
        uf = UserInfo()
    # return render_to_response('login.html', {'uf':uf},context_instance=RequestContext(req))
    return render_to_response('login.html', {'uf': uf})


# 登陆成功
def index(req):
    username = req.COOKIES.get('username', '')
    return render_to_response('index.html', {'username': username})


# 退出
def logout(req):
    response = HttpResponse('logout !!')

    # 清理cookie里保存username
    response.delete_cookie('username')
    return response


def showUser(req):
    userlist = models.User.objects.all()
    return render(req, 'showUser.html', {'userlist':userlist})


def addSong(req):
    if req.method == 'POST':
        sf = SongInfo(req.POST)
        if sf.is_valid():

            # 获得表单数据
            song_name = sf.cleaned_data['song_name']
            song_singer_name = sf.cleaned_data['song_singer_name']

            # 如果有此歌手
            singer = Singer.objects.filter(singer_name__exact=song_singer_name)
            if singer:
                pass
            else:
                Singer.objects.create(singer_name=song_singer_name)
            # 歌曲歌手重复
            singer = Singer.objects.filter(singer_name__exact=song_singer_name)
            song = Song.objects.filter(song_name__exact=song_name, song_singer_id__exact=singer.id)
            if song:
                return render_to_response('add_song.html', {'sf': sf})
            else:
                # 添加到数据库
                Song.objects.create(song_name=song_name, song_singer_id=singer.id)
                return HttpResponse('add success!!')

        else:
            print(45)
    else:
        print(req.method)
        uf = UserInfo()
        return render_to_response('user_Register.html', {'uf': uf})


def addSinger(req):
    if req.method == 'POST':
        sf = SingerInfo(req.POST)
        if sf.is_valid():

            # 获得表单数据
            singer_name = sf.cleaned_data['singer_name']
            singer_gender = sf.cleaned_data['singer_gender']
            singer_msg = sf.cleaned_data['singer_msg']

            # 如果有此歌手
            singer = Singer.objects.filter(singer_name__exact=singer_name)
            if singer:
                return render_to_response('add_singer.html', {'sf': sf})
            else:
                # 添加到数据库
                Song.objects.create(singer_name=singer_name, singer_gender=singer_gender, singer_msg=singer_msg)
                return HttpResponse('add success!!')
        else:
            print(45)
    else:
        print(req.method)
        sf = SingerInfo()
        return render_to_response('add_singer.html', {'sf': sf})


def addAlbum(req):
    if req.method == 'POST':
        af = AlbumInfo(req.POST)
        if af.is_valid():
            # 获得表单数据
            album_singer_name = af.cleaned_data['album_singer_name']
            album_name = af.cleaned_data['album_name']
            album_data = af.cleaned_data['album_data']

            singer = Singer.objects.filter(singer_name=album_singer_name)
            if singer:
                pass;
            else:
                return render_to_response('add_album.html', {'af': af})
            # 如果有此专辑同样歌手
            albumAndSinger = Album.objects.filter(album_singer_id_exact=singer.id, album_singer_name=album_singer_name)
            if albumAndSinger:
                return render_to_response('add_album.html', {'af': af})
            else:
                # 添加到数据库
                Album.objects.create(album_singer_id_exact=singer.id, album_singer_name=album_singer_name, album_data=album_data)
                return HttpResponse('add success!!')
        else:
            print(45)
    else:
        print(req.method)
        af = AlbumInfo()
        return render_to_response('add_singer.html', {'af': af})


def addLike(req):
    if req.method == 'POST':
        lf = Like(req.POST)
        if lf.is_valid():
            # 获得表单数据
            like_song_name = lf.cleaned_data['like_song_name']
            user_name = req.COOKIES['username']
            user_id = User.objects.filter(user_name=user_name)

            # 是否有该歌曲
            song = Song.objects.filter(song_name=like_song_name)
            if song:
                songlike = SongLikes.objects.filter(like_user_id=user_id, like_song_id=song.song_id)
                if songlike:
                    return render_to_response('song_info.html', {'af': lf})
                SongLikes.objects.create(like_user_id=user_id, like_song_id=song.song_id)
                return HttpResponse('mark success!!')
            else:
                return render_to_response('song_info.html', {'af': lf})
        else:
            print(45)
    else:
        print(req.method)
        lf = Like()
        return render_to_response('add_singer.html', {'lf': lf})


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
