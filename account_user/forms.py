from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'이메일을 입력하세요.'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control','placeholder':'비밀번호를 입력하세요.'})
        }
        labels = {
            'email': 'email',
            'password': 'password'
        }


