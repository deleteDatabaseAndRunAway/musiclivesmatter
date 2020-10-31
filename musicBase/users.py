from django.forms import widgets
from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django import forms
from musicBase import models
from musicBase.models import *
from django.contrib import messages


class UserInfo(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', max_length= 100)



class UserRegistInfo(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', max_length=100)
    repeat_password = forms.CharField(label='确认密码', max_length=100)
    user_gender = forms.CharField(label='性别',
        widget=widgets.Select(choices=[(1,"女"),(2,"男"),]),
        initial=1
    )
    user_com_type = forms.ChoiceField(label='请选择联系方式',
        choices=[(1, "QQ"),(2, "微信"),(3, "微博"),(4, "GitHub")], #单选下拉框
        initial=2
    )
    user_com = forms.CharField(label='具体联系方式',max_length=30)


def regist(req):
    if (req.method == 'GET'):
        uf = UserRegistInfo()
        print(uf)
        return render_to_response('user_Register.html', {'uf': uf})
    if (req.method == 'POST'):
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
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(user_name__exact=username, password__exact=password)
            if user:
                response = HttpResponseRedirect('/musicBase')
                return response
            return HttpResponse('no such User!')
    else:
        uf = UserInfo()
    return render_to_response('user_delete.html', {'uf': uf})
    # return render_to_response('register.html', {'uf': uf}, context_instance=RequestContext(req))


# 登陆
def login(req:HttpRequest):
    if req.method == 'POST':
        uf = UserInfo(req.POST)
        username = req.POST['username']
        password = req.POST['userPassword']
        print(username)
        user = User.objects.filter(user_name__exact=username, password__exact=password)
        print(user)
        if user:
            response = redirect(reverse('musicBase:index'))

            response.set_cookie('username', username, 3600)
            print(req.COOKIES.get('username'))
            return response
        else:

            # 比较失败，还在login
            return HttpResponseRedirect('/musicBase/login/')
    elif req.method == 'GET':
        return render_to_response('user_login.html')
    else:
        uf = UserInfo()
    return render_to_response('index.html', {'uf': uf})


def logout(req : HttpRequest):
    response = HttpResponse('logout !!')
    response.delete_cookie('username')
    return render_to_response('index.html')
