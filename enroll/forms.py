from django import forms
from django.db.models import fields
from django.forms import widgets 
from .models import User
class StudentRegestration(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name','email','password')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control','placeholder':'Enter Strong Password'}),
        }
        error_messages = {
            'name':{'required':'Enter Your Name'},
            'email':{'required':'Enter Your Email'},    
            'password':{'required':'Enter Password'},
        }