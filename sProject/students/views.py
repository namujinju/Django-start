from django.shortcuts import render
from django.http import HttpResponseRedirect  # 추가
from django.urls import reverse  # 추가
from students.models import Student  # 추가


def regStudent(request):
    return render(request, "registerStudent.html")
# return render(request, "students/registerStudent.html")
# 예제에선 이렇게 했는데 template를 못 찾는 오류가 있었음.


def regConStudent(request):
    name = request.POST["name"]
    major = request.POST["major"]
    age = request.POST["age"]
    grade = request.POST["grade"]
    gender = request.POST["gender"]
    # 괄호가 아니라 대괄호로. 이것 때문에 몇 시간 날림

    qs = Student(s_name=name, s_major=major, s_age=age,
                 s_grade=grade, s_gender=gender)
    qs.save()

    # stuAll는 urls의 name 이름
    return HttpResponseRedirect(reverse("students:stuAll"))


def reaStudentAll(request):
    qs = Student.objects.all()
    context = {"student_list": qs}
    return render(request, "readStudents.html", context)


def detStudent(request, name):
    qs = Student.objects.get(s_name=name)
    context = {'student_info': qs}
    return render(request, "detailStudent.html", context)


def reaStudentOne(request, name):
    qs = Student.objects.get(s_name=name)
    context = {'student_info': qs}
    return render(request, "modifyStudent.html", context)


def modConStudent(request):

    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']

    s_qs = Student.objects.get(s_name=name)

    s_qs.name = name
    s_qs.major = major
    s_qs.age = age
    s_qs.grade = grade
    s_qs.gender = gender

    s_qs.save()

    return HttpResponseRedirect(reverse("students:stuAll"))


def delConStudent(request, name):
    s_qs = Student.objects.get(s_name=name)
    s_qs.delete()
    return HttpResponseRedirect(reverse("students:stuAll"))
