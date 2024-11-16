# custom_admin/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .decoraters import admin_only
from django.http import HttpResponseForbidden
from Home_App.models import cvTemplateClass
from django.contrib.auth import login, authenticate, logout


@login_required
@admin_only
def dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Access Denied: Admins Only")
    user_count = User.objects.count()
    user_obj = User.objects.all()
    sendcv_obj = cvTemplateClass.objects.count()
    return render(request, 'dashboard.html', {'user_obj':user_obj, 'user_count':user_count, 'sendcv_obj': sendcv_obj})


def cvDetail(request):
    cv_obj = cvTemplateClass.objects.all()
    return render(request, 'cv.html', {'cv_obj':cv_obj})

def userDetail(request, user_id):
    user_obj = get_object_or_404(cvTemplateClass, id=user_id)
    return render(request, 'user-detail.html', {'user_obj': user_obj})

def addUser(request):
    if request.method == 'POST':
        # Retrieve form data and create or update CV
        full_name = request.POST.get('full_name')
        photo = request.FILES.get('photo')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        social_media = request.POST.get('social_media')
        languages = request.POST.get('languages')
        skills = request.POST.get('skills')
        education = request.POST.get('education')
        experience = request.POST.get('experience')

        sendData = cvTemplateClass(
            fullName=full_name,
            photo=photo,
            contactNumber=contact,
            email=email,
            address=address,
            socialMediaLinks=social_media,
            languages=languages,
            skills=skills,
            education=education,
            experience=experience
        )
        sendData.save()
    return render(request, 'add-user.html')


def updateUser(request, user_id):
    # Get the existing user record by ID
    try:
        existing_user = cvTemplateClass.objects.get(id=user_id)
    except cvTemplateClass.DoesNotExist:
        return render(request, 'error.html', {'message': 'User not found.'})

    if request.method == 'POST':
        # Form data retrieve karke existing user record update karenge
        existing_user.fullName = request.POST.get('full_name', existing_user.fullName)
        existing_user.photo = request.FILES.get('photo', existing_user.photo)
        existing_user.contactNumber = request.POST.get('contact', existing_user.contactNumber)
        existing_user.email = request.POST.get('email', existing_user.email)
        existing_user.address = request.POST.get('address', existing_user.address)
        existing_user.socialMediaLinks = request.POST.get('social_media', existing_user.socialMediaLinks)
        existing_user.languages = request.POST.get('languages', existing_user.languages)
        existing_user.skills = request.POST.get('skills', existing_user.skills)
        existing_user.education = request.POST.get('education', existing_user.education)
        existing_user.experience = request.POST.get('experience', existing_user.experience)

        # Record save karke update kar denge
        existing_user.save()
        
        # Redirect or render success message
        return render(request, 'success.html', {'message': 'User updated successfully.'})
    
    # Agar method POST nahi hai toh form render karega
    return render(request, 'update-user.html', {'user': existing_user})


def deleteUser(request, user_id):
    # Try to get the user by ID
    try:
        user_to_delete = cvTemplateClass.objects.get(id=user_id)
    except cvTemplateClass.DoesNotExist:
        return render(request, 'error.html', {'message': 'User not found.'})

    

    # Delete the user record
    user_to_delete.delete()

    # Redirect to a success page or any other page after deletion
    return redirect('cv-detail') 


# def register_superuser(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         # Superuser create karenge
#         user = User.objects.create_superuser(username=username, password=password)
#         login(request, user)  # User ko login kar denge
#         return redirect('custom_dashboard')  # Redirect to a dashboard page
    
#     return render(request, 'register_superuser.html')

def login_superuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        # Agar user superuser hai toh login karega
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('custom_dashboard')  # Redirect to dashboard
        else:
            return render(request, 'login_superuser.html', {'error': 'Invalid credentials or not a superuser.'})
    
    return render(request, 'login_superuser.html')

def logout_superuser(request):
    logout(request)  # User ko logout kar dena
    return redirect('login-superuser') 