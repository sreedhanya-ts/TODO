from django.shortcuts import render
from django.contrib.auth.models import User
from .models import*
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
# Create your views here.
def homepage(request):
    return render(request,"home.html")


# def task(request):
#     return render(request, 'task.html')

def signup(request):
    print("signuppage")
    if request.method=="POST":
        print("form submission")
        user=User.objects.create(username=request.POST.get("username"))
        user.set_password(request.POST.get("password"))
        user.save()
        Profile.objects.create(
            user=user,
            firstname=request.POST.get("firstname"),
            lastname=request.POST.get("lastname"),
            email=request.POST.get("email"),
            image=request.FILES["image"],
            phone=request.POST.get("phone"),
            )
    return HttpResponseRedirect(reverse('homepage'))
def userlogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        print(user)
        if user:
            login(request,user)
            print("login successful")
    return HttpResponseRedirect(reverse("homepage"))

def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
def todoedit(request):
    return render(request,"edit.html")
def addtodo(request):
    todo=Todo.objects.filter(user=request.user)
    if request.method=="POST":
       Todo.objects.create(
        title=request.POST.get("task"),
        deadline=request.POST.get("date"),
        user=request.user
       )
       return HttpResponseRedirect(reverse("addtodo"))
    return render(request,"task.html",{'content':todo})
    
 

 
