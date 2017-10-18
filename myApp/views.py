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
    # student_list = Student.student_objects2.filter(student_grade_id=grade_id)

    # 加入模型管理类之后，就需要进行上面的替换这样的操作，
    # 可不可以直接覆盖objects？试一试，可以覆盖，这样就会省很多操作。
    student_list = Student.objects.filter(student_grade_id=grade_id)

    # # 获得对应的班级对象
    # grade = Grade.objects.get(pk=grade_id)
    #
    # # 获得班级下的所有学生对象列表
    # student_list = grade.student_set.all()

    # 仍然把上边的模板给它
    return render(request, 'myApp/students.html', {'students': student_list})


def add_student(request):
    grade = Grade.objects.get(pk=3)
    student = Student.objects.create(student_name="乔丹", student_age=50, student_gender=True,
                                     student_contend='篮球之神',
                                     student_grade=grade,
                                     create_time='2017-5-1', last_time='2017-10-17')
    # student = Student.objects.create_student("库里", 26, True, '库日天', grade, '2017-5-1', '2017-10-17')
    if student.student_gender:
        grade.grade_boy_num += 1
    else:
        grade.grade_girl_num += 1
    grade.save()
    student.save()
    return HttpResponse("student ok")


def student_page(request, page):
    """分页显示学生"""
    # 有漏洞，没有处理不存在的情况
    page = int(page)
    student_list = Student.objects.all()[(page - 1) * 5: page * 5]
    return render(request, "myApp/students.html", {"students": student_list})


def attribute(request):
    return HttpResponse('attributes: --'
                        'path:%s --'
                        'method:%s --'
                        'encoding:%s --'
                        'GET:%s --'
                        'POST:%s --'
                        'FILES:%s --'
                        'COOKIES:%s --'
                        'session:%s' % (request.path, request.method,
                                        request.encoding, request.GET,
                                        request.POST, request.FILES,
                                        request.COOKIES, request.session))


def get1(request):
    """获取get传递的数据，两种方式"""
    a = request.GET.get('a')
    b = request.GET['b']
    c = request.GET.get('c')
    return HttpResponse(a + "    " + b + "    " + c)


def get2(request):
    """获取get传递的数据, 一个键对应多个值"""
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET['c']
    return HttpResponse(a1 + "    " + a2 + "    " + c)


def show_register(request):
    return render(request, 'myApp/register.html')


def register(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    post = request.POST.getlist('hobby')
    return HttpResponse("<h1>register success</h1><br><hr>"
                        "<ol><li>%s</li><li>%s</li>"
                        "<li>%s</li><li>%s</li></ol>" % (name, gender, age, post))


def show_response(request):
    res = HttpResponse()
    print(res.content, res.charset, res.status_code)
    return res
