from django.conf.urls import url
from musicBase import views,users
from django.urls import path

app_name = 'musicBase'
urlpatterns = [path('', views.index, name='index'),
               path('login', users.login, name='login'),
               path('regist', users.regist, name='regist'),
               path('index', views.index, name='index'),
               path('logout', users.logout, name='logout'),
               path('delete_user',users.delet_user,name = 'delete_user'),
               ]
