from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.
def Student_View(request):
    
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print('data inserted successfully...')
    form = StudentForm()        
    return render(request,'testapp/modelform.html',{'form':form})