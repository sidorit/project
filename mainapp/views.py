from json import decoder
from django.shortcuts import render
from account_user.models import Fuser
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAccount
from .get_social_info import *
#파이썬 함수식으로 만들면 됨
def main(request):
    data = {}
    user_pk = request.session.get('user') #login 함수에서 추가해준 request.session['user'] = fuser.id
    try:
        social_account = SocialAccount.objects.all()[0]
        print('소셜 로그인 이름--> ',social_account.extra_data['name'])
        social_user_name = social_account.extra_data['name']
    except:
        social_account = None

    if social_account or user_pk :
        print('ㅇㅇ 소셜로 로그인  또는 아이디로 로그인했어 ')
    else:
        print('소셜로그인도 안했고 사이트 로그인도 안함')

    if user_pk: #세션에 user_pk 정보가 존재하면
        fuser = Fuser.objects.get(pk = user_pk)
        data['user'] = fuser
    elif social_account:
        request.session['social_user']= social_user_name #섹션에 소셜 유저의 이름만 저장하기. -->(다른 함수에서 get 하기 위해서.)
                                                                #기존에 사용자
        data['user'] = social_user_name
    else:
        data['temp'] = 1
    return render(request, "main.html",data)

def mypage(request):
    data={}
    print('실행')
    data['user'] = None  #처음에 base.html을 상속하기 때문에
    #data['user'] 의 값을 None으로 변경안하면 처음 main페이지의 user 값이랑 겹친다.
    user_pk = request.session.get('user')
    print( 'user_pk =', user_pk)
    social_name = request.session.get('social_user')
    try:
        fuser = Fuser.objects.get(pk=user_pk)
        data['user']=fuser
    except:
        data['social_user'] = social_name
    print(data)
    return render(request, "mypage.html", data)
    
def profile_modify(request):
    temp=0
    data={}
    user_pk = request.session.get('user')
    if request.method == 'GET':
        fuser = Fuser.objects.get(pk=user_pk)
        data['user']=fuser
        return render(request, "profile_modify.html", data)
    elif request.method == 'POST':
        fuser = Fuser.objects.get(pk=user_pk)
        fuser.useremail =request.POST.get('useremail')   
        fuser.school = request.POST.get('school')
        fuser.major = request.POST.get('major')
        fuser.grade = request.POST.get('grade')
        fuser.phone = request.POST.get('phone')
        if not (fuser.useremail and fuser.school and fuser.major and fuser.grade and fuser.phone):
            data['error']="⚠모든 칸을 입력해주세요⚠"    
            return render (request,"profile_modify.html",data) 
        else:
            fuser.save()
            data['user']=fuser
            return render (request,"mypage.html",data)
    



    #이 함수는 welcome이라는 이름 다른곳에서 welcome으로 불러올 수 있다. 
    #이 함수는 render라는 함수로 welcome.html을 띄워준다.

