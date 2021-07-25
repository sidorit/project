from django.contrib import admin
from .models import Fuser
# Register your models here.

class FuserAdmin(admin.ModelAdmin):
    list_display = ('username','password','useremail', 'school', 'major', 'grade', 'phone')

admin.site.register(Fuser,FuserAdmin)