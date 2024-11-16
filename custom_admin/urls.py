# custom_admin/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', login_superuser, name='login-superuser'),
    path('dashboard/', dashboard, name='custom_dashboard'),
    path('cv-detail/', cvDetail, name='cv-detail'),
    path('user-detail/<int:user_id>/', userDetail, name='user-detail'),
    path('add-user/', addUser, name='add-user'),
    path('update-user/<int:user_id>/', updateUser, name='update-user'),
    path('delete-user/<int:user_id>/', deleteUser, name='delete-user'),
    # path('register-superuser/', register_superuser, name='register-superuser'),
    path('logout-superuser/', logout_superuser, name='logout-superuser'),
]
