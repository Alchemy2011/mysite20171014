from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^index/$', views.index, name='index'),
]
