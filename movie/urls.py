from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

# 下面这种是在生产环境中配置静态文件和上传文件的方法，后面加上stctic等等，
# 但前提：需要在settings.py中配置STATIC_URL、STATIC_ROOT、MEDIA_URL、MEDIA_ROOT，
# 为了媒体文件不影响静态文件，所以static和media分开配置
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^detail/(?P<movie_id>\d+)/$', views.detail, name='detail'),
    url(r'^detail3', views.detail3, name='detail3'),
    url(r'^err/$', views.err, name='err'),
    url(r'^upload/$', views.upload, name='upload'),
]
