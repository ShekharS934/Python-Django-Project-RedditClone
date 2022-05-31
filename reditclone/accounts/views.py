from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.method=='POST':
        if request.POST['Password1']== request.POST['Password2']:
            try:
                user=User.objects.get(username=request.POST['Username'])
                return render(request, 'accounts/signups.html', {'error':'Oops! Username already taken!'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['Username'], password=request.POST['Password1'], )
                login(request, user)
                return render(request, 'accounts/signups.html')
        else:
            return render(request, 'accounts/signups.html', {'error':'Oops! Passwords Don''t match'})
    else:
        return render(request, 'accounts/signups.html')
    
    
def login_user(request):
    if request.method=='POST':
        user=authenticate(username=request.POST['Username'], password=request.POST['Password'])
        if user is not None:
            login(request, user)
            if request.POST['next'] is not None:
                return redirect(request.POST['next'])
            return redirect('home')
            
        else:
            return render(request, 'accounts/login.html', {'error':'Oops! Username and Passwords Don''t match'})
    else:
        return render(request, 'accounts/login.html')
    
    
def logoutview(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')
        
    