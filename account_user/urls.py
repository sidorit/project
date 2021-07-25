from django.contrib import admin
from django.urls import path,include
from . import views
#우리는 url로 웹사이트를 호출한다.


urlpatterns = [
    path('login/',views.signin ,name='login'),
    path('signup/',views.register,name='signup'),
    path('logout/',views.logout,name='logout'),

]
