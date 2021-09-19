
from django.shortcuts import render,HttpResponseRedirect
from django.urls.conf import include
from .forms import StudentRegestration
from .models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegestration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data.get('name')
            em = fm.cleaned_data.get('email')
            pw = fm.cleaned_data.get('password')
            # Save the data in database
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegestration() 
    else:
        fm = StudentRegestration()
    
    
    stud = User.objects.all()   
    return render(request,'enroll/add_data.html',{'form':fm,'std':stud})

#This function will Update/Edit the data
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegestration(request.POST,instance=pi)

        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegestration(instance=pi)
    return render(request,'enroll/update_show.html',{'form':fm})    

# This function will delete the data
def delete_data(request,id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)  
        data.delete()
        return HttpResponseRedirect('/')  