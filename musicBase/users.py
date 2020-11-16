from django.forms import widgets
from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django import forms
from musicBase import models
from musicBase.models import *
from django.contrib import auth
from django.contrib import messages


class UserInfo(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', max_length= 100)



class UserRegistInfo(forms.Form):
    email = forms.EmailField(label='电子邮箱')
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', max_length=100)
    repeat_password = forms.CharField(label='确认密码', max_length=100)
    user_gender = forms.CharField(label='性别')
    user_com = forms.CharField(label='具体联系方式',max_length=30)
    user_birthday = forms.DateField(label='您的生日')


def regist(req):
    if (req.method == 'POST'):
        print("req : %s\n" % req)
        uf = UserRegistInfo(req.POST)
        print(uf.errors)
        if uf.is_valid():
            cleaned = uf.clean()
            if User.objects.filter(email=cleaned['email']):
                return render(req, 'user_Register.html', {'uf': uf, 'msg': "此邮箱已注册！"})
            if cleaned['password'] != cleaned['repeat_password']:
                return render(req, 'user_Register.html', {'uf': uf, 'msg': "请输入相同的密码！"})
            del cleaned['repeat_password']
            User.objects.create_user(**cleaned)
            return render(req,'index.html', {'msg':"注册成功！"})
        else:
            return render(req,'user_Register.html', {'uf':uf,'msg':"输入信息有格式问题！"})
    uf = UserRegistInfo()
    return render(req,'user_Register.html', {'uf':uf})


def delet_user(req):
    if req.method == 'POST':
        uf = UserInfo(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(user_name__exact=username, password__exact=password)
            if user:
                response = redirect("musicBase:index")
                return response
            return HttpResponse('no such User!')
    else:
        uf = UserInfo()
    return render(req,'user_delete.html', {'uf': uf})


# 登陆
def login(req:HttpRequest):
    if req.method == 'POST':
        uf = UserInfo(req.POST)
        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user:
            auth.login(req,user)
            req.session['username'] = username
            return render(req,'index.html')
        else:
            return render(req,'user_login.html',{'msg':"用户名或密码错误！"})
    uf = UserInfo()
    return render(req,'user_login.html')


def logout(req : HttpRequest):
    auth.logout(req)
    return redirect(reverse('musicBase:index'))

def update_user_info(req : HttpRequest):
    print(req.user.username)
    return render(req,'update_user_info.html')


def user_index(req:HttpRequest,user_id):
    user_now = User.objects.get(id=user_id)
    likes = SongLikes.objects.filter(like_user_id=user_now)
    return render(req,'personalPage.html',{'user':user_now,'likes':likes})


def compare_likes(req:HttpRequest,another_user_id):
    my_likes = SongLikes.objects.filter(like_user_id=req.user)
    another = User.objects.get(id=another_user_id)
    another_likes = SongLikes.objects.filter(like_user_id=another_user_id)
    my_like_song_num = len(my_likes)
    similar = 0
    for i in my_likes:
        if SongLikes.objects.get(like_user_id=another,like_song_id=i.like_song_id):
            similar += 1
    if my_like_song_num > 0:
        similar = similar / my_like_song_num
    return render(req,'compare_likes.html',{'another':another,'similar':similar})
