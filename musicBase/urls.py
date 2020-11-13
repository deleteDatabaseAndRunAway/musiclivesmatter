from django.conf.urls import url
from musicBase import views,users
from django.urls import path

app_name = 'musicBase'
urlpatterns = [path('', views.index, name='index'),
               path(r'login', users.login, name='login'),
               path(r'regist', users.regist, name='regist'),
               path(r'index', views.index, name='index'),
               path(r'logout', users.logout, name='logout'),
               path(r'delete_user',users.delet_user,name = 'delete_user'),
               path(r'update_user_info',users.update_user_info,name = 'update_user_info')
               ]
