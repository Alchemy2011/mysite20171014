import os

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Movie


# Create your views here.
def index(request):
    movie_list = Movie.objects.all().filter(is_ban=False)

    return render(request, 'movie/index.html', {'movie_list': movie_list})


def detail(request, movie_id):
    try:
        movie = get_object_or_404(Movie, pk=movie_id)
    except:
        return render(request, 'movie/err.html', {'err_message': '查询错误'})
    else:
        return render(request, 'movie/detail.html', {'movie': movie})


def detail3(request):
    # movie_id = request.GET['movie_id']
    # get方法比较安全，但还不是最好，最佳方案是使用get_objects_or_404快捷方式
    movie_id = request.GET.get('movie_id', default=None)
    try:
        if movie_id is not None:
            movie = Movie.objects.get(pk=movie_id)
    except:
        # return HttpResponse('<h3>错误的电影id</h3>')，这是演示反向解析
        return HttpResponseRedirect(reverse('movie:err'))
    else:
        return render(request, 'movie/detail.html', {'movie': movie})


def err(request, movie_id):
    # 使用快捷键模块，是为了保持松散耦合
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie/err.html', {'movie': movie})


def upload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_path = os.path.join(settings.MEDIA_ROOT, file.name)
        with open(file_path, 'wb') as fp:
            for info in file.chunks():
                fp.write(info)
    return HttpResponse('上传文件成功')
