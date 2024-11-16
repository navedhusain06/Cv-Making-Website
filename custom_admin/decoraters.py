# custom_admin/decorators.py
from django.http import HttpResponseForbidden

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("Access Denied: Admins Only")
        return view_func(request, *args, **kwargs)
    return wrapper_func
