from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

#用户列表
class Users(AbstractBaseUser):
    account = models.CharField(max_length=32, unique=True) #账户
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=255) #姓名
    avatar = models.TextField() #头像
    role = models.CharField(max_length=10, default='user')  # 角色
    created_at = models.DateTimeField(auto_now_add=True) #创建
    updated_at = models.DateTimeField(auto_now=True) #更新
    deleted_at = models.DateTimeField(default=None).blank  # 标记删除

    USERNAME_FIELD = 'account'
    REQUIRED_FIELDS = ['name']

    #获取姓名缩写
    def get_short_name(self):
        return self.name
    #获取全名
    def get_full_name(self):
        return self.name
    #获取用户名
    def get_username(self):
        return self.name

    objects = UserManager()


    class Meta:
        db_table = u'users'