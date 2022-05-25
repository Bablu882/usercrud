
from .models import User
from django import forms

class UserRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','mobile','city']
        # Widgets={
        #     'name': forms.TextInput(attrs={"class":"form-control"}),
        #     'email': forms.EmailInput(attrs={"class":"form-control"}),
        #     'mobile': forms.TextInput(attrs={"class":"form-control"}),
        #     'city': forms.TextInput(attrs={"class":"form-control"}),
        # }

        
