from django.forms import widgets
from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django import forms
from musicBase import models
from musicBase.models import *

class DeleteSingerInfo(forms.Form):
    singer_name = forms.CharField(label='歌手名', max_length=100)

class SingerInfo(forms.Form):
    singer_name = forms.CharField(label='歌手名', max_length=100)
    singer_gender = forms.CharField(label='性别',max_length=20)
    singer_msg = forms.CharField(label='歌手信息')

#增
def add_singer(req:HttpRequest):
    if (req.method == 'GET'):
        uf = SingerInfo()
        return render(req,'add_singer.html', {'uf': uf})
    if (req.method == 'POST'):
        print("req : %s\n" % req)
        uf = SingerInfo(req.POST)
        print(uf.errors)

        if uf.is_valid():
            cleaned = uf.clean()
            singer_exist = Singer.objects.filter(singer_name__exact=cleaned['singer_name'])
            if singer_exist:
                print("singer exist!")
            else:
                singer = Singer.objects.create(**cleaned)
                return HttpResponse('add song success!!')
    return render(req,'add_singer.html', {'uf': uf,'script':"alert",'wrong':"添加歌曲失败！"})

#删
def delete_singer(req):
    if req.method == 'POST':
        uf = DeleteSingerInfo(req.POST)
        if uf.is_valid():
            cleaned = uf.clean()
            singer_to_delete = Singer.objects.filter(singer_name__exact=cleaned['singer_name'])
            if singer_to_delete:
                singer_to_delete.delete()
                return HttpResponse('delete singer success!!')
            return HttpResponse('no such Singer!')
    else:
        uf = DeleteSingerInfo()
    return render(req,'delete_singer.html', {'uf': uf})

#展示
def singer_showall(req:HttpRequest):
    singers = Singer.objects.filter()
    return render(req,'singer_showall.html',{'singers':singers})
"""class SingersShowAll(ListView):
    model = Singer
    template_name = 'singer_showall.html'
    context_object_name = 'singer_list'"""


#查

