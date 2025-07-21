from django.shortcuts import render
from django.contrib.auth.models import User
from .models import*
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
# Create your views here.
def homepage(request):
    return render(request,"home.html")