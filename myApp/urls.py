from django.conf.urls import url
from django.conf.urls.static import static

from myApp import views
from mysite import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/(\d+)/$', views.detail, name='detail'),  # 正则中分组的概念
    url(r'^grades/$', views.grades, name='grades'),
    url(r'^students/$', views.students, name='students'),
    url(r'^grades/(\d+)/$', views.grade_students, name='grade_students'),
    url(r'^addstudent/$', views.add_student, name='add_student'),
    url(r'^studentpage/(\d+)/$', views.student_page, name='student_page'),
    url(r'^attribute/$', views.attribute, name='attribute'),
    url(r'^get1/$', views.get1, name='get1'),
    url(r'^get2/$', views.get2, name='get2'),
    url(r'^showregister/$', views.show_register, name='show_register'),
    url(r'^register/$', views.register, name='register'),
    url(r'^showresponse/$', views.show_response, name='show_response'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
