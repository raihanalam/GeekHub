from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Home/home.html')

def profile(request):
    return render(request,'Home/profile.html')