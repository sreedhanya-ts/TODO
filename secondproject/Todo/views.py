from django.shortcuts import render
from django.contrib.auth.models import User
from .models import*
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
# Create your views here.
def homepage(request):
    try:
        profile = Profile.objects.filter(user=request.user).first()
    except:
        profile = None
    return render(request, "home.html", {"profile": profile})


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
    
def todocomplete(request,pk):
     complete=Todo.objects.filter(pk=pk).first()
     complete.complete=True
     complete.save()
     return HttpResponseRedirect(reverse("addtodo"))
    
def todoclose(request,pk):
     close=Todo.objects.filter(pk=pk).first()
     close.complete=False
     close.save()
     return HttpResponseRedirect(reverse("addtodo"))

def deletetodo(request,pk):
   todo=Todo.objects.filter(pk=pk).first()
#    print(todo)
   todo.delete()
   return HttpResponseRedirect(reverse("addtodo"))

def edittodo(request,pk):
     todo=Todo.objects.filter(pk=pk).first()
    # print(todo)
     if request.method=="POST":
        todo.title=request.POST.get("Task")
        todo.deadline=request.POST.get("date")
        todo.save()
        return HttpResponseRedirect(reverse("addtodo"))
     return render(request,"edit.html",{"todo":todo})

def editprofile(request,pk):
    print("edit profile")
    profile = Profile.objects.filter(pk=pk).first()
    if request.method=="POST":
       if request.FILES.get("image"):
        profile.image=request.FILES.get("image")
       profile.firstname=request.POST.get("firstname")
       profile.lastname=request.POST.get("lastname")
       profile.email=request.POST.get("email")
       profile.phone=request.POST.get("phone")
       profile.save()

    return HttpResponseRedirect(reverse('homepage'))



 
