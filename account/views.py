from django.shortcuts import render,redirect, reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        userName = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=userName).exists():
                messages.error(request, 'Username already exist!')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exist!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=userName, password=password, email=email)
                user.save()
                return redirect('signin')
        else:
            messages.warning(request, 'Password and confirm password doesnt match')
            return redirect('signup')
    return render(request,'Account/signup.html')

def signin(request):
    if request.method == 'POST':
        userName=request.POST['username']
        password =request.POST['password']
        user = authenticate(request,username=userName,password=password)

        if user is not None:
            login(request,user)
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Invalid Username or Password!')
            return redirect('signin')
    else:
        return render(request,'Account/signin.html')
def signout(request):
    logout(request)
    messages.success(request, 'Successfully Logout!!.')
    return redirect('signin')

def recovery(request):
    return render(request,'Account/recovery.html')

