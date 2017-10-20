# coding: utf-8
import os

from django.contrib.auth import logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

# 从哪导入settings，有问题
from django.conf import settings
# from mysite import settings
from myApp.task import celery_demo
from myApp.models import Grade, Student


def index(request):
    # return HttpResponse('myApp is a good app')
    # 这里有问题，如果粗存在就会报错。
    student = Student.objects.get(pk=3)
    return render(request, 'myApp/index.html',
                  {'num': 666, 'stu': student, 'str': "myApp is a good app.",
                   'test': 777, 'code': "<h1>myApp is a escape app.</h1>"})


def index1(request):
    return HttpResponseRedirect('/myapp')


def detail(request, num, num2):
    return HttpResponse("detail-%s-%s" % (num, num2))


def grades(request):
    # 视图去模板里取数据
    grade_list = Grade.objects.all()
    # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回浏览器
    return render(request, 'myApp/grades.html', {'grades': grade_list})


def students(request):
    student_list = Student.objects.all()
    # Show 25 students per page
    paginator = Paginator(student_list, 5)

    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range(e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)
    return render(request, 'myApp/students.html',
                  {'students': students, 'student_list': student_list})


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
    # student.save()
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


def cookie_test(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write("<h1>" + cookie["myApp"] + "</h1>")
    # cookie = res.set_cookie("myApp", 'better')
    return res


def redirect1(request):
    """重定向需要的是地址，是路径"""
    # return HttpResponseRedirect("/myapp/redirect2")
    # 可以使用html中url解析的格式, namespace和name不变，那么下面就不需要改动
    return redirect("myApp:redirect2")
    # 也可以传url路径
    # return redirect("/myapp/redirect2")


def redirect2(request):
    return HttpResponse("我是重定向地址，后的视图")


def main(request):
    # 取session
    username = request.session.get('username', default='游客')
    return render(request, 'myApp/main.html', {'username': username})


def login(request):
    return render(request, 'myApp/login.html')


def show_main(request):
    username = request.POST.get('username')

    # 存储session
    request.session['username'] = username

    # 设置过期时间，单位:秒
    # request.session.set_expiry(10)
    return redirect("/myapp/main")


def my_logout(request):
    # 退出时，清除session
    logout(request)
    # request.session.clear()
    # request.session.flush()
    return redirect("/myapp/main")


def good(request, page):
    """
    html中反向解析url传过来的参数必须接，
    合成的url要和urls正则中的匹配，
    有几个参数，就需要有几个圆括号。
    """
    return render(request, 'myApp/good.html', {'num': page})


def better(request):
    return render(request, 'myApp/better.html')


def home(request):
    return render(request, 'myApp/home.html')


def csrf(request):
    return render(request, 'myApp/csrf.html')


def show_csrf(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    return render(request, 'myApp/showcsrf.html',
                  {'username': username, 'password': password})


def verify_code(request):
    """生成验证码图片"""
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont

    # 引入随机模块函数
    import random

    # 自定变量， 用于画面的背景色、宽、高
    back_ground_color = (random.randrange(20, 100),
                         random.randrange(20, 100),
                         random.randrange(20, 100))
    width = 100
    height = 50

    # 创建画面对象
    im = Image.new('RGB', (width, height), back_ground_color)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    strings = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(4):
        rand_str += strings[random.randrange(0, len(strings))]
    # 构造字体对象
    font = ImageFont.truetype(r'C:\Windows\Fonts\Microsoft YaHei UI\MSYH.TTC', 40)
    # 构造字体颜色
    font_color1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    font_color2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    font_color3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    font_color4 = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=font_color1)
    draw.text((25, 2), rand_str[1], font=font, fill=font_color2)
    draw.text((50, 2), rand_str[2], font=font, fill=font_color3)
    draw.text((75, 2), rand_str[3], font=font, fill=font_color4)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verify'] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将突破保持在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端， MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def verify_code_file(request):
    f = request.session.get("flag")
    strings = ''
    if f is False:
        strings = "请重新输入"
    request.session.clear()
    return render(request, 'myApp/verifycodefile.html', {'flag': strings})


def verify_code_check(request):
    code1 = request.POST.get("verify_code").upper()
    code2 = request.session["verify"].upper()
    if code1 == code2:
        return render(request, 'myApp/verifycuccess.html')
    else:
        request.session['flag'] = False
        return redirect("myApp:verify_code_file")


def upload(request):
    return render(request, 'myApp/upload.html')


def save_file(request):
    """上传文件必须是post请求"""
    if request.method == 'POST':
        file = request.FILES.get('file')
        # 合成文件在服务器端的路径
        file_path = os.path.join(os.path.join(settings.MEDIA_ROOT,
                                              'myApp/upload'), file.name)
        with open(file_path, 'wb') as fp:
            # 以文件流的形式一段一段接收
            for info in file.chunks():
                fp.write(info)
        return HttpResponse('上传成功')
    else:
        return HttpResponse("上传失败")


def ajax_students(request):
    return render(request, 'myApp/ajaxstudents.html')


def students_info(request):
    students = Student.objects.all()
    lists = []
    for student in students:
        lists.append([student.student_name, student.student_age])
    return JsonResponse({"data": lists})


def edit(request):
    return render(request, 'myApp/edit.html')


def celery(request):
    """分布式任务调度模块，解决耗时操作和执行定时任务"""
    # 添加到celery中执行，不会阻塞。但是还需要环境，需要启动redis和work
    celery_demo.delay()
    return render(request, 'myApp/celery.html')
