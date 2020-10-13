from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from musicBase.models import User


# 表单
class UserInfo(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', max_length= 100)


# 注册
def regist(req):
    if req.method == 'POST':
        uf = UserInfo(req.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 添加到数据库
            User.objects.create(username=username, password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserInfo()
    return render_to_response('register.html', {'uf': uf})
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
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                # 比较成功，跳转index
                response = HttpResponseRedirect('/musicBase/index/')
                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username,3600)
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
