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
    user_gender = forms.CharField(label='性别',
        widget=widgets.Select(choices=[(1,"女"),(2,"男"),]),
        initial=1
    )
    user_com_type = forms.ChoiceField(label='请选择联系方式',
        choices=[(1, "微信"),(2, "QQ"),(3, "微博"),(4, "GitHub")], #单选下拉框
        initial=2
    )
    user_com = forms.CharField(label='具体联系方式',max_length=30)
    user_birthday = forms.DateField(label='您的生日')
    user_show_message = forms.ChoiceField(label='是否向其他用户展示个人信息',
        choices=[(True,"是"),(False,"否"),],
        initial=False
    )
    user_show_likes = forms.ChoiceField(label='是否向其他用户展示歌曲喜好',
        choices=[(True,"是"),(False,"否"),],
        initial=True
    )
    def clean_user_email(self):
        user_email = self.cleaned_data['email']
        users = User.objects.filter(email=user_email)
        if users:
            raise forms.ValidationError("此邮箱已注册")
        return user_email
    def clean_repeat_password(self):
        pwd = self.cleaned_data['password']
        rpwd = self.cleaned_data['repeat_password']
        if pwd != rpwd:
            raise forms.ValidationError("请输入相同的密码！")
        return pwd


def regist(req):
    if (req.method == 'GET'):
        uf = UserRegistInfo()
        return render_to_response('user_Register.html', {'uf': uf})
    if (req.method == 'POST'):
        print("req : %s\n" % req)
        uf = UserRegistInfo(req.POST)
        print(uf.errors)
        if uf.is_valid():
            cleaned = uf.clean()
            del cleaned['repeat_password']
            user = User.objects.create_user(**cleaned)
            return HttpResponse('regist success!!')
    return render_to_response('user_Register.html', {'uf': uf,'script':"alert",'wrong':"是不是出什么问题啦！"})


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
            response = redirect(reverse('musicBase:index'))
            return response
        else:
            return redirect(reverse('musicBase:login'))
    elif req.method == 'GET':
        return render_to_response('user_login.html')
    return render_to_response('user_login.html')


def logout(req : HttpRequest):
    response = HttpResponse('logout !!')
    auth.logout(req)
    return redirect(reverse('musicBase:index'))

def update_user_info(req : HttpRequest):
    print(req.user.username)
    return render(req,'update_user_info.html')
