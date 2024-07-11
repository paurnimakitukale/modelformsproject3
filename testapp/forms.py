from django import forms
from testapp.models import Student
class StudentForm(forms.ModelForm):
    name = forms.CharField(max_length=60)
    rollno = forms.IntegerField()
    address = forms.CharField(max_length=60)
    email = forms.EmailField()
    class Meta:
        model = Student
        fields = '__all__'