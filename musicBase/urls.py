from django.conf.urls import url
from musicBase import views
from django.urls import path

app_name = 'musicBase'
urlpatterns = [path(r'^$', views.login, name='login'),
               path(r'^login/$', views.login, name='login'),
               path(r'^regist/$', views.regist, name='regist'),
               path(r'^index/$', views.index, name='index'),
               path(r'^logout/$', views.logout, name='logout'),
               path(r'^delete_user/$',views.delet_user,name = 'delete_user'),
               ]
