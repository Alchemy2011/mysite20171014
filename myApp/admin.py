# coding: utf-8
from django.contrib import admin

# Register your models here.
from .models import Grade, Student


# 扁平方式：创建班级的时候顺便添加学生，就需要表格内联
class StudentInfo(admin.TabularInline):
    model = Student
    extra = 2


# # 堆栈方式
# class StudentInfo(admin.StackedInline):
#     model = Student
#     extra = 2

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    # 决定具体内联哪个表格
    inlines = [StudentInfo]

    # 列表页属性
    list_display = ['pk', 'grade_name', 'grade_date', 'grade_girl_num',
                    'grade_boy_num', 'is_delete']
    list_filter = ['grade_name']
    list_per_page = 5
    search_fields = ['grade_name']

    # 添加、修改页属性
    # fields = ['grade_girl_num', 'grade_boy_num', 'grade_name', 'grade_date', 'is_delete']
    # 将字段分组，但这两条不能同时使用。使用列表和元组都可以，只要能够索引就行。
    fieldsets = [
        ("num", {"fields": ['grade_girl_num', 'grade_boy_num']}),
        ("base", {"fields": ['grade_name', 'grade_date', 'is_delete']}),
    ]
    # fieldsets = [
    #     ["num", {"fields": ['grade_girl_num', 'grade_boy_num']}],
    #     ["base", {"fields": ['grade_name', 'grade_date', 'is_delete']}],
    # ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        """用自定义的字段内容，替换原有字段默认显示的问题"""
        if self.student_gender:
            return "男"
        else:
            return "女"

    # 设置页面列的名称
    gender.short_description = "性别"  # 改变字段显示，简短描述

    list_display = ['pk', 'student_name', 'student_age', gender,
                    'student_contend', 'student_grade', 'create_time', 'last_time']
    list_per_page = 2

    # 执行动作的位置问题，如果只设置一个会上下都有显示
    actions_on_top = False
    actions_on_bottom = True


# 以后使用装饰器进行注册，下面这句就省了
# admin.site.register(Grade, GradeAdmin)
# admin.site.register(Student, StudentAdmin)
