# coding:utf8
from django.db import models

'''
电影模型
名字
上映时间，
片长，
又名，

    导演 多对多
    编剧 多对多
    演员 多对多
    类型 多对多
    国家/地区 多对一
    语言 多对一
'''


# 电影模型的管理类，这样在不删除数据库里禁播的数据的情况下，
# 实现了在站点后台看不到禁播数据的目的
class MovieManager(models.Manager):
    def get_queryset(self):
        return super(MovieManager, self).get_queryset().filter(is_ban=False)


# 人类信息的父类
class Person(models.Model):
    pname = models.CharField(max_length=128, verbose_name='姓名')
    pxingbie = models.BooleanField(default=True, verbose_name='性别')
    pchusheng = models.DateTimeField(auto_now_add=True, verbose_name='出生日期')
    pchushengdi = models.CharField(max_length=64, verbose_name='出生地')
    pjianjie = models.TextField(verbose_name='简介')
    purl = models.CharField('肖像', max_length=512)

    def __str__(self):
        return self.pname

    class Meta:
        # 代表这个模型是一个虚拟模型，在迁移时不会被编译
        abstract = True


class Guojia(models.Model):
    gjname = models.CharField(max_length=32)

    def __str__(self):
        return '国家: %s.' % self.gjname


class Diqu(models.Model):
    dqname = models.CharField(max_length=32)

    def __str__(self):
        return '地区: %s.' % self.dqname


class Yuyan(models.Model):
    lname = models.CharField(max_length=32)

    def __str__(self):
        return '语言: %s.' % self.lname


class Movie(models.Model):
    # movie_objects = MovieManager()
    # 下面这种操作是原来操作的优化版本，这样似乎就不会改变原来的接口
    objects = MovieManager()

    mname = models.CharField(max_length=128)
    shangying = models.DateField(auto_now_add=True)
    pianchang = models.IntegerField(default=90)
    youming = models.CharField(max_length=128)
    jianjie = models.TextField()
    url = models.CharField(verbose_name='封面', max_length=512)
    is_ban = models.BooleanField(default=False)

    # 通过Django Console创建的时候需要传入对象，例如国家对象，而不是名字
    guojia = models.ForeignKey(Guojia)
    diqu = models.ForeignKey(Diqu)
    yuyan = models.ForeignKey(Yuyan)

    def __str__(self):
        return '电影: %s' % self.mname

    class Meta:
        # db_table
        ordering = ['shangying']


class Daoyan(Person):
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return '导演: %s.' % self.pname


class Bianju(Person):
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return '编剧: %s.' % self.pname


class Yanyuan(Person):
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return '演员: %s.' % self.pname


class Leixing(models.Model):
    lxname = models.CharField(max_length=32)

    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return '类型: %s.' % self.lxname
