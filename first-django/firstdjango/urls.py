"""firstdjango URL Configuration

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
from django.contrib import admin
from django.urls import path, include # include 불러와야 함
from first import views # first는 패키지 이름

urlpatterns = [
    path("", include("first.urls")), # 웹앱 별로 다른 url 규칙을 적용하기 위해, 웹앱을 여러 개 만들어야 하기 때문에 관리를 용이하게
    path('admin/', admin.site.urls)
]
