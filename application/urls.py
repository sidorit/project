from django.contrib import admin
from django.urls import path,include
from . import views
#우리는 url로 웹사이트를 호출한다.


urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/<int:id>',views.detail, name='detail'),
    path('submit/', views.submit, name="submit"),
    path('finish/', views.finish, name="finish"),
    path('edit/', views.edit, name="edit"),
    path('apply_modify/', views.apply_modify, name="apply_modify"),
    path('apply_modify/<str:username>/', views.apply_modify, name="apply_modify"),
]
  