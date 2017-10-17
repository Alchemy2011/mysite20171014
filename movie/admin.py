from django.contrib import admin

from .models import *
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['mname', 'shangying', 'pianchang', 'guojia', 'diqu', 'yuyan']



class GuojiaAdmin(admin.ModelAdmin):
    list_display = ['gjname']

class YanyanAdmin(admin.ModelAdmin):
    list_display = ['yyname','']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Guojia, GuojiaAdmin)
admin.site.register(Diqu)
admin.site.register(Yanyuan)