from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm 
from django.template import RequestContext
from django.contrib import auth
from allauth.socialaccount.models import SocialAccount #소셜로그인 후 로그아웃 할려고

from .models import Fuser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password

def signin(request):
    res_data ={}
    res_data['temp'] = 1
    if request.method=="GET":
        return render(request,'login.html',res_data)
    elif request.method == "POST" :
        #전송받은 이메일 비밀번호 확인
        useremail = request.POST.get('useremail')
        password = request.POST.get('password')
    
        #유효성 처리
        
        if not (useremail and password):
            res_data['error']="⚠️모든 값을 입력해야 합니다⚠️"
        else:
            # 기존(DB)에 있는 Fuser 모델과 같은 값인 걸 가져온다.
            # 회원 유무 확인
            try:
                fuser = Fuser.objects.get(useremail = useremail) #(필드명 = 값)
            except:
                return render(request, "loginFail.html", res_data)
            # 없는 회원인 경우.. 수정하면 좋을 듯
            # 비밀번호가 맞는지 확인한다. 위에 check_password를 참조
            if check_password(password, fuser.password):
                #응답 데이터 세션에 fuser의 기본키(pk)값인 id 추가. 나중에 쿠키에 저장됨
                request.session['user']=fuser.id #세션에 저장 -> 로그인 후 세션이 저장됌.
                #리다이렉트
                return redirect('/')
            else:
                res_data['error'] = "⚠️비밀번호가 틀렸습니다⚠️"

        return render(request,'login.html',res_data) #응답 데이터 res_data 전달

# forms.py 를 이용한 로그인 구현
# def signin(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         email = request.POST['id_email']
#         password = request.POST['id_password']
#         user = authenticate(request=request,email = email, password = password)
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#         else:
#             return HttpResponse('로그인 실패. 다시 시도 해보세요.')
#     else:
#         form = LoginForm()
#         return render(request, 'login.html',{'form':form})





def register(request):   #회원가입 관련 함수
    res_data ={} #프론트에 던져줄 응답 데이터
    res_data['temp'] = 1 #로그인 안한 상태이니까.
    if request.method == "GET":
        return render(request, 'sign.html',res_data)
    elif request.method == "POST":
        #여기에 회원가입 처리 코드
        # username = request.POST['username']
        # password = request.POST['password']
        # re_password = request.POST['re-password']
      
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password',None)
        useremail = request.POST.get('useremail',None)
        school = request.POST.get('school', None)
        major = request.POST.get('major', None)
        grade = request.POST.get('grade', None)
        phone = request.POST.get('phone', None)
        

        #option 빼고 모든 값을 입력해야됨
        if not( username and password and re_password and useremail and school and major and grade and phone):
        # if not( username and password and re_password and useremail): #None은 False로 인식
            res_data['error']="⚠️모든 값을 입력해야 합니다⚠️"
        #비밀번호가 다르면 리턴
        elif password != re_password:
            # return HttpResponse("비밀번호가 다름")
            res_data['error']="⚠️비밀번호가 다름⚠️"
        #같으면 저장
        else : 
            #위 정보들로 인스턴스 생성
            fuser = Fuser(
                username= username,
                password= make_password(password),
                useremail = useremail,
                school = school,
                major = major,
                grade = grade,
                phone = phone,
            )
            
            #저장
            fuser.save()
            return render(request, 'signFinish.html', res_data)

        return render(request, 'sign.html',res_data)

def logout(request):
    data = {}
    social_user = SocialAccount.objects.all()
    print(social_user)
    try:
        user =  request.session['user']
    except:
        user = None
    if user:
        del(request.session['user'])
    elif social_user:
        del(request.session['social_user'])
        social_user.delete()
    else: #소셜도 기존 로그인도 아님
        data['error'] = '로그인중이 아님'
    return redirect('/')

