# 更新日志

自2020.10.19开始记录

### 更新时间：10.19.19:20
**作者：** wyk  
**更新内容：**   
修复了views.regist使用的表单与user_Register数据名不一致导致无法成功注册的bug
更改了index.html中的超连接方法  
更改了models.py中的数据定义，使其与外键关联

**改动文件：**
```
bighomework/urls.py
musigBase/urls.py
musicBase/views.py
musicBase/models.py
templates/add_album.html
templates/add_singer.html
templates/index.html
templates/user_Register.html
```
