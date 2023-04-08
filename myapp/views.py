from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def signuppage(request):
    msg=''
    if request.method=='POST':
        fm=Signupform(request.POST)
        print(fm)
        if fm.is_valid():
            fm.save()
            msg='Account created succussfully!!!'
    else:
        fm= Signupform()
    return render(request,'signup.html',{'form':fm,'msg':msg})


def loginpage(request):
    if request.method == 'POST':
        fm= AuthenticationForm(data=request.POST, request=request)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            print('username:',username)
            print('password:',password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/dashboard/')
    else:
        fm= AuthenticationForm()
    return render(request, 'login.html',{'form':fm})


def dashboardpage(request):
    return render(request,'dashboard.html')


def logoutpage(request):
    logout(request)
    return HttpResponseRedirect('/login/')

