from django.shortcuts import redirect, render
from .forms import CustomRegisterform
from django.contrib import messages 

def register(request):
    if request.method == "POST": 
       register_form = CustomRegisterform(request.POST)
       if register_form.is_valid(): 
           register_form.save() 
           messages.success(request, ("New user account created . Login to get Started"))
           return redirect('register')
    else: 
       register_form = CustomRegisterform()

    return render(request, 'register.html' ,{'register_form': register_form})
