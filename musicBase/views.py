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
    song_name = forms.CharField(label='歌名',max_length=50)
    song_singer_name = forms.CharField(label='歌手名',max_length=50)


# 注册
def regist(req):
    if (req.method == 'POST') | (req.method == 'GET'):
        print("req : %s\n", req)
        uf = UserRegistInfo(req.GET)
        print("uf : %s\n", uf)
        print(uf.cleaned_data)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            repeat_password = uf.cleaned_data['repeat_password']

            # 用户名重复吗
            user = User.objects.filter(user_name__exact=username)
            print("35\n")
            if user:
                if password != repeat_password:
                    print(uf.password)
                    print(uf.repeat_password)
                    return render_to_response('user_Register.html', {'uf': uf})

            # 添加到数据库
            User.objects.create(user_name=username, password=password)
            return HttpResponse('regist success!!')
        else:
            print(45)
    else:
        print(req.method)
        uf = UserInfo()
    return render_to_response('user_Register.html', {'uf': uf})
    # return render_to_response('register.html', {'uf': uf}, context_instance=RequestContext(req))


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
            # 比较失败报错
            # User.objects.create(username=username, password=password)
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
    if (req.method == 'POST') | (req.method == 'GET'):
        sf = SongInfo(req.GET)
        if sf.is_valid():
            # 获得表单数据
            song_name = sf.cleaned_data['song_name']
            song_singer_name = sf.cleaned_data['song_singer_name']

            # 歌曲名重复吗
            song = Song.objects.filter(song_name__exact=song_name, song_singer_name__exact=song_singer_name)
            if song:
                return render_to_response('add_song.html', {'sf': sf})

            # 添加到数据库
            Song.objects.create(song_name=song_name, song_singer_name=song_singer_name)
            return HttpResponse('add success!!')
        else:
            print(45)
    else:
        print(req.method)
        uf = UserInfo()
    return render_to_response('user_Register.html', {'uf': uf})
