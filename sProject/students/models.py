#
from django.db import models

# Create your models here.
# ORM: (Object Relational Mapping) SQL문을 클래스로 매핑해서 좀 더 사용자가 사용하기 쉽게 만듦


class Student(models.Model):  # models 클래스를 상속
    s_name = models.CharField(max_length=100)  # s_name은 필드 이름
    s_major = models.CharField(max_length=100)
    s_age = models.IntegerField(default=0)
    s_grade = models.IntegerField(default=0)
    s_gender = models.CharField(max_length=100)

    def __str__(self):
        return self.s_name

# admin 파일에 추가해야 함


# Create: qs = Student(~~~), qs.save()

# Read: Student.objects.all(), Student.objects.get(조건)
# 데이터 필터
# (__lt, __lte, __gt, __gte, __isnull, __contains, __startwith, __endwith)
# 데이터 정렬
# .order_by(" ") 오름차순
# .order_by(" ") 내림차순

# Update
# 필드 값으로 접근해서 값을 바꾸기 save()까지 붙여야 함.
