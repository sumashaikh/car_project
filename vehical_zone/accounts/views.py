from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages,auth
from django.contrib.auth.models import User


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid login creadentials')
            return redirect('login')

    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username all ready exists')
                print(messages)
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email all ready exists')
                    return redirect('register')
                else:
                    user=User.objects.create(first_name=firstname,last_name=lastname,
                        username=username,password=password)
                    auth.login(request,user)
                    messages.success(request,'you are now login')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request,"you are registerd successfully")
                    return redirect('login')
        else:
            messages.error(request,'This is error message')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request,'you are successfully logged out')
        return redirect('home')
    return redirect('home')  # Redirect to the 'home' named URL pattern within the 'pages' app
