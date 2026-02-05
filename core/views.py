from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Memory
from django.contrib.auth.models import User
from django.http import JsonResponse
from PIL import Image
from django.contrib import messages
from .forms import RegisterForm, LoginForm

# Login
def login_view(request):
    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')

    return render(request, 'core/login.html', {'form': form})


# Register
def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')

    return render(request, 'core/register.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')


# Dashboard
def dashboard(request):
    return render(request, 'core/dashboard.html')



# Dashboard
def dashboard(request):
    return render(request,'core/dashboard.html')

# Memory
def memory(request):
    if request.method=="POST":
        Memory.objects.create(user=request.user,text=request.POST['text'])
    data = Memory.objects.filter(user=request.user)
    return render(request,'core/memory.html',{'data':data})


# ML Drawing API (dummy similarity)
def ml_draw(request):
    if request.method=="POST":
        img_file=request.FILES['image']
        img=Image.open(img_file)
        similarity=80
        return JsonResponse({"similarity":similarity})
