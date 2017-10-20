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
    url(r'^cookietest/$', views.cookie_test, name='cookie_test'),
    url(r'^redirect1/$', views.redirect1, name='redirect1'),
    url(r'^redirect2/$', views.redirect2, name='redirect2'),
    url(r'^index.html$', views.index1, name='index1'),
    url(r'^main/$', views.main, name='main'),
    url(r'^login/$', views.login, name='login'),
    url(r'^showmain/$', views.show_main, name='show_main'),
    url(r'^logout/$', views.my_logout, name='my_logout'),
    url(r'^good/(\d+)/$', views.good, name='good'),
    url(r'^better/$', views.better, name='better'),
    url(r'^home/$', views.home, name='home'),
    url(r'^csrf/$', views.csrf, name='csrf'),
    url(r'^showcsrf/$', views.show_csrf, name='show_csrf'),
    url(r'^verifycode/$', views.verify_code, name='verify_code'),
    url(r'^verifycodefile/$', views.verify_code_file, name='verify_code_file'),
    url(r'^verifycodecheck/$', views.verify_code_check, name='verify_code_check'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^savefile/$', views.save_file, name='save_file'),
    url(r'^ajaxstudents/$', views.ajax_students, name='ajax_student'),
    url(r'^studentsinfo/$', views.students_info, name='students_info'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^celery/$', views.celery, name='celery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
