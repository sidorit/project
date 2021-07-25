from django.db import models

# Create your models here.

# 지원서 
# 한 줄 소개 , 지원동기, 만들고 싶은 사이트 -> 이유 , 프로젝트 경험 , 갈등 -> 해결방법

class User_Application(models.Model):  # models.Model를 상속

    username = models.CharField(max_length=32,verbose_name='사용자명')
    one_introduction = models.CharField(max_length=100,verbose_name='한 줄 소개')
    motive = models.TextField(verbose_name='지원동기')
    make_site = models.TextField(verbose_name='만들고 싶은 사이트')
    why = models.TextField(verbose_name='이유')
    project_experience = models.TextField(verbose_name='경험')
    conflict =models.TextField(verbose_name='갈등')
    solution = models.TextField(verbose_name='해결방법')
    state = models.TextField(verbose_name='합불상태', default='지원 완료', blank=True)
    
    update_time = models.DateTimeField(auto_now=True) #해당 레코드 갱신시 현재 시간이 자동 저장함.


    #데이터가 문자열로 변환이 될 때 어떻게 나올지(반환해줄지) 정의하는 함수가 __str__이다.
    def __str__(self):
        return self.one_introduction


    #별도로 테이블명을 지정하고 싶을 때 쓰는 코드(안해도 됨)
    class Meta:
        db_table = 'User_Application_table' #테이블 명 지정
        verbose_name = '지원서' #노출될 테이블 이름 변경
        verbose_name_plural = '지원서'
