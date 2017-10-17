# coding: utf-8
from django.db import models


# Create your models here.
class Grade(models.Model):
    grade_name = models.CharField(max_length=64)
    grade_date = models.DateTimeField()
    grade_girl_num = models.IntegerField()
    grade_boy_num = models.IntegerField()
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.grade_name

class Student(models.Model):
    student_name = models.CharField(max_length=64)
    student_gender = models.BooleanField(default=True)
    student_age = models.IntegerField()
    student_contend = models.CharField(max_length=64)
    is_delete = models.BooleanField(default=False)

    # 关联外键
    student_grade = models.ForeignKey("Grade")

    def __str__(self):
        return self.student_name
