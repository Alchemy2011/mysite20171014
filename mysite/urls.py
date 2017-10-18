"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# 为了测试，另外配置的欢迎页面
from polls import views

urlpatterns = [
    url(r'^myapp/', include('myApp.urls', namespace='myApp')),
    url(r'^bbs/', include('bbs.urls', namespace='bbs')),
    url(r'^movie/', include('movie.urls', namespace='movie')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^$', views.hello_django),
    url(r'^admin/', admin.site.urls),
]
