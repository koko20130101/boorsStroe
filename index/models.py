from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='书名')
    public = models.CharField(max_length=50, verbose_name='出版社')
    price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='定价')

    def default_price():
        return '￥30'
    retail_price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name='零售价', default=default_price)

    def __str__(self):
        return 'title:%s pub:%s price:%s' % (self.title, self.public, self.price)


class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')

    def __str__(self):
        return '作者：%s' % (self.name)


class UserInfo(models.Model):
    username = models.CharField(max_length=24, verbose_name='用户注册')
    password = models.CharField(max_length=24, verbose_name='密码')
    choices = (
        ('male', '男性'),
        ('female', '女性'),
    )
    gender = models.CharField(
        max_length=2, choices=choices, default='male', verbose_name='性别')
