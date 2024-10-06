from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginFun(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)
        
        if not user_obj.exists():
            messages.error(request, 'User Does not Exists')
            return redirect('loginNm')
        
        user_obj = authenticate(username = email, password = password)
        if user_obj:
            login(request, user_obj)
            return redirect('homeNm')
        messages.error(request, 'Incorrect Email and password')
        return redirect('loginNm')
        
    return render(request, 'login.html')

def registerFun(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)
        
        if user_obj.exists():
            messages.warning(request, 'Email already exists')
            return redirect('registerNm')
        
        user_obj = User.objects.create(first_name=firstname, last_name=lastname, email=email, username=email)
        user_obj.set_password(password)
        user_obj.save()
        
        messages.success(request, 'Your Account Are successfully Created')
        return redirect('loginNm')

    return render(request, 'register.html')
def logoutFun(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homeNm')
    return render(request, 'logout.html')
