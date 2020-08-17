from django.shortcuts import render
from django.http import HttpResponseRedirect  # 추가
from django.urls import reverse
from board.models import User


def signupUser(request):
    return render(request, "signup.html")


def signConUser(request):
    name = request.POST["name"]
    nickname = request.POST["nickname"]
    age = request.POST["age"]

    qs = User(u_name=name, u_nickname=nickname, u_age=age)
    qs.save()

    return HttpResponseRedirect(reverse("board:index"))


def postAll(request):
    qs = User.objects.all()
    context = {"user_list": qs}
    return render(request, "index.html", context)


def userListAll(request):
    qs = User.objects.all()
    context = {"user_list": qs}
    return render(request, "userList.html", context)


def userDetail(request, name):
    qs = User.objects.get(u_name=name)
    context = {"user_info": qs}
    return render(request, "detailUser.html", context)


def modUser(request, name):
    qs = User.objects.get(u_name=name)
    context = {"user_info": qs}
    return render(request, "modUser.html", context)


def modUserCon(request):
    name = request.POST["name"]
    nickname = request.POST["nickname"]
    age = request.POST["age"]

    qs = User.objects.get(u_name=name)
    qs.u_nickname = nickname
    qs.u_age = age
    qs.save()

    return HttpResponseRedirect(reverse("board:userList"))


def delUser(request, name):
    qs = User.objects.get(u_name=name)
    qs.delete()
    return HttpResponseRedirect(reverse("board:userList"))
