from django.db import models
from allauth.account import *

# Create your models here.

# 이름 , 학교 (학과 , 학번), 이메일 , 
# 전화번호, 성별, 입학년도, ( 선택사항 - 깃허브,인스타그램)

class Fuser(models.Model):  # models.Model를 상속
    username = models.CharField(max_length=32,
                                verbose_name='사용자명'  # admin 페이지에서 보일 컬럼명
                                )
    useremail = models.EmailField(max_length=128,      
                                verbose_name='사용자이메일'  # admin 페이지에서 보일 컬럼명
                                )
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호'  # admin 페이지에서 보일 컬럼명
                                )
    school = models.CharField(max_length=64,
                                verbose_name='학교'
                                )
    major = models.CharField(max_length=64,
                                verbose_name='학과'
                                )
    grade = models.CharField(max_length=64,
                                verbose_name='학년'
                                )
    phone = models.CharField(max_length=64,
                                verbose_name='전화번호'
                                )
    register_dttm = models.DateField(auto_now_add=True, # 자동으로 해당 시간이 추가됨
                                     verbose_name="가입날짜"
                                )


    #데이터가 문자열로 변환이 될 때 어떻게 나올지(반환해줄지) 정의하는 함수가 __str__이다.
    def __str__(self):
        return self.username


    #별도로 테이블명을 지정하고 싶을 때 쓰는 코드(안해도 됨)
    class Meta:
        db_table = 'user_define_fuser_table' #테이블 명 지정
        verbose_name = '사용자 모임' #노출될 테이블 이름 변경
        verbose_name_plural = '사용자 모임'
