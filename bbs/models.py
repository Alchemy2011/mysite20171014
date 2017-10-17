from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
class BbsUser(models.Model):
    user = models.OneToOneField(User)

    # 改用系统自带的User
    # username = models.CharField(max_length=64)
    # password = models.CharField(max_length=64)
    # email = models.EmailField()

    phone = models.IntegerField()
    sex = models.BooleanField()
    head_image = models.ImageField(upload_to="avatar/", default="avatar/default.jpg")

    def __str__(self):
        return self.user.username


class Post(models.Model):
    # 如果找不到，引起来就行了。
    # author = models.ForeignKey("User")
    author = models.ForeignKey(User)
    content = models.TextField()
    title = models.CharField(max_length=128)
    summary = models.CharField(max_length=256, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)  # 创建时就增加时间
    modify_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category")

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 级联，一起删掉

    def __str__(self):
        return "creator:%s" % (self.creator)  # ??


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
