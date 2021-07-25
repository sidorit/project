"""lionproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from mainapp import views
from django.contrib import admin
from django.urls import path,include
#우리는 url로 웹사이트를 호출한다.

#url등록하는 것
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main , name="main"),
    path('account/',include('account_user.urls'),name='account'),
    path('application/', include('application.urls'),name="application"),
    path('mypage/', views.mypage, name="mypage"),
    path('profile_modify/', views.profile_modify, name="profile_modify"),
    #앞에 아무것도 안적으면 서버를 처음 구동시키고 나오는 페이지가 main이 되게 한다.
    #다른 html에서 url 대신에 main이라는 이름을 사용할 수 있다.

    path('accounts/',include('allauth.urls')), #로깅 추가

]
