# coding: utf-8
from django.db import models


# Create your models here.
from tinymce.models import HTMLField


class Grade(models.Model):
    grade_name = models.CharField(max_length=64, unique=True)
    grade_date = models.DateTimeField()
    grade_girl_num = models.IntegerField()
    grade_boy_num = models.IntegerField()
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.grade_name

    class Meta:
        db_table = "grade"


class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(is_delete=False)

    # 创建对象的方法二:
    # def create_student(self, name, age, gender, contend, grade, create_time, last_time, is_delete=False):
    #     student = self.model()
    #     student.student_name = name
    #     student.student_age = age
    #     student.student_gender = gender
    #     student.student_contend = contend
    #     student.student_grade = grade
    #     student.last_time = last_time
    #     student.create_time = create_time
    #     student.save()
    #     return student


class Student(models.Model):
    # 自定义模型管理器，如果只是创建管理类的实例，而不修改，和原始的objects没有qubie
    # student_objects = models.Manager()
    # 不能同时存在，否则不起作用。需要注意:原来views中objects需要替换为student_objects2
    # student_objects2 = StudentManager()

    # 为了省去后边该很多的麻烦，我觉得可以直接利用赋值去覆盖原有的objects
    objects = StudentManager()

    student_name = models.CharField(max_length=64)
    student_age = models.IntegerField(db_column='age')
    student_gender = models.BooleanField(default=True)
    student_contend = models.CharField(max_length=64)
    is_delete = models.BooleanField(default=False)

    # 关联外键
    student_grade = models.ForeignKey("Grade")

    create_time = models.DateTimeField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_name

    def get_name(self):
        """演示在模板中调用方法时，随便引入"""
        return self.student_name

    class Meta:
        """设置数据表的元信息，例如改变默认的数据表名，由appname_模型名，改为自定义"""
        db_table = "student"
        ordering = ['id',
                    # '-id',  # 倒序
                    ]

    # 方法一：在模型中，定义一个类方法创建对象；方法二在模型管理类中
    # 其实创建模型管理类实例对象后，覆盖了默认的objects，连下面的方法定义也可以省略了，就用原来的接口
    # 其实如果用了新名称，而没有覆盖，仍然可以用原来的方式创建对象。
    # @classmethod
    # def create_student(cls, name, age, gender, contend, grade, create_time, last_time, is_delete=False):
    #     student = cls(student_name=name, student_age=age,
    #                   student_gender=gender,student_contend=contend,
    #                   student_grade=grade, create_time=create_time,
    #                   last_time=last_time, is_delete=is_delete)
    #     return student

class Text(models.Model):
    # 富文本编辑器，效果似乎一般
    content = HTMLField()