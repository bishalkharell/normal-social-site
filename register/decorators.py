
from django.http import request
from django.shortcuts import redirect

def restrictPages(func_view):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:       
            return func_view(request,*args,**kwargs)

    return wrapper

