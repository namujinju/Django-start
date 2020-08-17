"""myBoard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path('signup/', views.signupUser, name="signup"),
    path('signCon/', views.signConUser, name="signCon"),
    path('index/', views.postAll, name="index"),
    path('userlist/', views.userListAll, name="userList"),
    path('<str:name>/userdet/', views.userDetail, name="userDet"),
    path('<str:name>/modUser/', views.modUser, name="modUser"),
    path('modUserCon/', views.modUserCon, name="modUserCon"),
    path('<str:name>/delUser/', views.delUser, name="delUser"),

]
