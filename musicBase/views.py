from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django import forms
from musicBase import models
from musicBase.models import *

from django.views.decorators.csrf import csrf_exempt


# 登陆成功
def index(req:HttpRequest):
    print(req.user.is_authenticated)
    return render(req,'index.html')

def showUser(req):
    userlist = models.User.objects.all()
    return render(req,'showUser.html', {'userlist':userlist})



def addComment(req):
    if req.method == 'POST':
        # user_name = req.COOKIES['username']
        # user_id = User.objects.filter(user_name=user_name)
        song_name = req.POST['song_name']
        comment_msg = req.POST['comment']
        comment_song_id = Song.objects.filter(song_name=song_name).id
        SongLikes.objects.create(comment_song_id=comment_song_id, comment_msg=comment_msg)
        return HttpResponse("comment success")


def music_manage(req:HttpRequest):
    return render(req,'musicManage.html')
