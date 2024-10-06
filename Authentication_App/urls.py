from django.urls import path
from .views import *

urlpatterns = [
    path('', loginFun, name='loginNm'),
    path('register/', registerFun, name='registerNm'),
    path('logout/', logoutFun, name='logoutNm'),
]
