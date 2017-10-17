# coding: utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Grade, Student


def index(request):
    return HttpResponse('myApp is a good app')


def detail(request, num, num2):
    return HttpResponse("detail-%s-%s" % (num, num2))


def grades(request):
    # 视图去模板里取数据
    grade_list = Grade.objects.all()
    # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回浏览器
    return render(request, 'myApp/grades.html', {'grades': grade_list})


def students(request):
    student_list = Student.objects.all()
    return render(request, 'myApp/students.html', {'students': student_list})


def grade_students(request, grade_id):
    """点击班级，显示该班级的所有学生"""
    # 在多的一方直接过滤就能获得
    student_list = Student.objects.filter(student_grade_id=grade_id)

    # # 获得对应的班级对象
    # grade = Grade.objects.get(pk=grade_id)
    #
    # # 获得班级下的所有学生对象列表
    # student_list = grade.student_set.all()

    # 仍然把上边的模板给它
    return render(request, 'myApp/students.html', {'students': student_list})
