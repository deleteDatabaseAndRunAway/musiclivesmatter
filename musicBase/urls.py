from django.conf.urls import url
from musicBase import views,users,albums,songs,singers
from django.urls import path

app_name = 'musicBase'
urlpatterns = [path('', views.index, name='index'),
               path(r'login', users.login, name='login'),
               path(r'regist', users.regist, name='regist'),
               path(r'index', views.index, name='index'),
               path(r'logout', users.logout, name='logout'),
               path(r'delete_user', users.delet_user, name='delete_user'),
               path(r'update_user_info', users.update_user_info, name='update_user_info'),
               path(r'add_song', songs.addSong, name='add_song'),
               path(r'add_singer', singers.add_singer, name='add_singer'),
               path(r'add_album', albums.addAlbum, name='add_album'),
               path(r'singer_showall',singers.singer_showall,name='singer_showall'),
               path(r'album_showall',albums.album_showall,name='album_showall'),
               path(r'song_showall',songs.song_showall,name='song_showall'),
               path('song_index/<int:song_id>',songs.song_index,name='song_index'),
               path('song_like/<int:song_id>',songs.like_song,name='song_like'),
               path('user_index/<int:user_id>',users.user_index,name = 'user_index'),
               path('music_mange',views.music_manage,name='music_manage')
               ]
