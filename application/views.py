#1
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
#2
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

from .models import User_Application
from account_user.models import Fuser    


def index(request):
    data = {}
    user_pk = request.session.get('user')
    fuser = Fuser.objects.get(pk=user_pk)
    data['user'] = fuser
    sort = request.GET.get('sort','') #url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다
    if sort == 'submit_date': #지원한 순서대로 정렬
        all_boards = User_Application.objects.all().order_by("update_time")
        data['Board_List'] = all_boards
        return render(request, 'index.html', data)
    elif sort == 'name': #이름순으로 정렬
        user = request.user
        all_boards = User_Application.objects.all().order_by("username")
        data['Board_List'] = all_boards
        return render(request, 'index.html', data)
    elif sort == 'new_date': #최신순으로 정렬
        all_boards = User_Application.objects.all().order_by("-update_time")
        data['Board_List'] = all_boards
        return render(request, 'index.html', data)
    else: #기본값은 최신값순으로 정렬
        all_boards = User_Application.objects.all().order_by("-update_time")
        data['Board_List'] = all_boards
        return render(request, 'index.html', data)

def detail(request, id):
    data = {}
    user_pk = request.session.get('user')
    fuser = Fuser.objects.get(pk=user_pk)
    data['user'] = fuser
    board = User_Application.objects.get(id=id)
    data['app'] = board
    if request.method == "GET":
        return render(request, 'detail.html', data)
    elif request.method == "POST": 
        board.state = request.POST.get('state')
        board.save(update_fields=['state'])
        data['app'] = board
        return redirect('/application/index/')

def finish(request):
    return render(request, "finish.html")


def edit(request):
    data = {}
    social_name = request.session.get('social_user') #없으면 None
    user_pk = request.session.get('user')
    try:
        fuser = Fuser.objects.get(pk=user_pk)
        myname = fuser.username
        apply = User_Application.objects.get(username=myname)
        data['app'] = apply
        return render(request, 'edit.html', data)
    except:
        apply = User_Application.objects.get(username=social_name)
        data['app'] = apply
    return render(request, 'edit.html', data)

def apply_modify(request,username):
    data = {}
    apply = User_Application.objects.get(username=username)
    if request.method == 'GET':
        data['app']=apply
        return render(request, "apply_modify.html", data)
    elif request.method == 'POST':
        apply_m = User_Application.objects.get(username=username)
        apply_m.one_introduction = request.POST.get('intro_line')
        apply_m.motive = request.POST.get('motivation')
        apply_m.make_site = request.POST.get('page')
        apply_m.why = request.POST.get('why')
        apply_m.project_experience = request.POST.get('project_experience')
        apply_m.conflict = request.POST.get('conflict')
        apply_m.solution = request.POST.get('solution')

        apply_m.save()
        data['user']=apply_m
        return render (request,"modify_finish.html",data)


def modify_finish(request):
    return render(request, "modify_finish.html")



def submit(request):
    data = {}
    if request.method == "GET":
        user_pk = request.session.get('user') #없으면 None
        social_name = request.session.get('social_user') #없으면 None
        
        try:
            social = User_Application.objects.get(username=social_name)
            return redirect('/application/edit/')
        except:
            pass
        try:
           fuser = Fuser.objects.get(pk=user_pk)
           print('zzzzzzzzzzzz트라이 : ',fuser)
           user_app =  User_Application.objects.get(username=fuser.username)
           print('zzddkdkdkdkdkdk : ',user_app)
           return redirect('/application/edit/')
        except:
            data['user'] = fuser.username
            data['social_user'] = social_name
            return render(request,'submit.html',data)
            

    elif request.method == "POST":
        new_person = User_Application()
        new_person.one_introduction = request.POST.get('intro_line')
        new_person.motive = request.POST.get('motivation')
        new_person.make_site = request.POST.get('page')
        new_person.project_experience = request.POST.get('project_experience')
        new_person.conflict = request.POST.get('conflict')

        new_person.solution = request.POST.get('solution')
        new_person.why = request.POST.get('why')
        new_person.username = request.POST.get('name')
        # new_person.state = request.POST.get('state')  이 부분때매 오류가 났어요~

        new_person.save()
        return redirect('finish')