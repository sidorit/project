import os
import sys
import urllib.request


def social_user_Info(access_token):
    print('소셜 유저 인포 ㅇㅇ 실행')
    token = access_token
    print('여기야?',token)
    header = "Bearer " + token # Bearer 다음에 공백 추가
    print('header =',header)
    url = "https://openapi.naver.com/v1/nid/me"
    request = urllib.request.Request(url)
    request.add_header("Authorization", header)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    print(response)
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
