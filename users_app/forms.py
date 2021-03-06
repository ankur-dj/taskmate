from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterform(UserCreationForm): 
    email = forms.EmailField(help_text='Enter an Valid Email Address')
    first_name = forms.CharField( max_length= 30, required=False , help_text='Optional')
    last_name =  forms.CharField( max_length= 30, required=False , help_text='Optional')
    
    
    class Meta: 
        model = User
        fields = ['username','first_name' , 'last_name','email', 'password1' , 'password2' ,  ]
  

