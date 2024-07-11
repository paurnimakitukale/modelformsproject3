from django.contrib import admin
from testapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','rollno','address','email']
admin.site.register(Student,StudentAdmin)    