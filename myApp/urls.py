from django.conf.urls import url

from myApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/(\d+)/$', views.detail, name='detail'),  # 正则中分组的概念
    url(r'^grades/$', views.grades, name='grades'),
    url(r'^students/$', views.students, name='students'),
    url(r'^grades/(\d+)/$', views.grade_students, name='grade_students'),
]
