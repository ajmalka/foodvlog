from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth



# Create your views here.
def registration(request ):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
        else:
            print("password not matched")
            messages.info(request,"password not matched")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,"invalid details")
            return redirect("login")
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')