from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODOO
from django.contrib.auth import authenticate, login,logout


def signup(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        # Here you would typically save the user to the database
        print(fnm,email,pwd)
        my_user=User.objects.create_user(fnm,email,pwd)
        my_user.save()
        return redirect('/login')
    return render(request, 'signup.html')


def loginn(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/home')
        else:
            return redirect('/home')
    return render(request, 'loginn.html')


def home(request):
     if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.TODOO(title=title, user=request.user)
        obj.save()
        res=models.TODOO.objects.filter(user=request.user).order_by('-date')
        return redirect('/home',{res:'res'})
     res=models.TODOO.objects.filter(user=request.user).order_by('-date')
     return render(request, 'home.html',{'res': res})


def edit_todo(request,srno):
     if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
         # Retrieve 'sron' from the POST request
        obj = models.TODOO.objects.get(srno=srno)
        obj.title=title
        obj.save()
        user=request.user
        
        return redirect('/home',{obj:'obj'})
     
     obj=models.TODOO.objects.get(srno=srno)
    
     return render(request, 'home.html')


def delete_todo(request,srno):
    obj =models.TODOO.objects.get(srno=srno)
    obj.delete()
    return redirect('/home')  


def signout(request):
    logout(request)
    return redirect('/loginn')