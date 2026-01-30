from django.shortcuts import render ,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'register.html')


# LOGIN
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "login successfully")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')


# LOGOUT
def user_logout(request):
    logout(request)
    messages.success(request, "logout sussessfully")
    return redirect('login')

def index(request):
    return render(request, 'index.html')