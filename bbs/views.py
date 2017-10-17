import os

from django.conf import settings
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import *


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponse("login success")
        else:
            return render(request, 'bbs/login.html', {'login_err': "username or password is wrong"})
    else:
        return render(request, 'bbs/login.html')


def index(request):
    categroy_list = Category.objects.all()
    post_list = Post.objects.all()
    data = {
        'category_list': categroy_list,
        'post_list': post_list,
    }
    return render(request, 'bbs/index.html', data)


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'bbs/post_detail.html')
