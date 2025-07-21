from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms




class Sign(UserCreationForm):
    birth_date = forms.DateField(required=True,help_text='Format: YYYY-MM-DD')
    name=forms.CharField(max_length=200,help_text='Your first name')
    class Meta:
     model = User 
     fields = ('name','username', 'birth_date', 'password1', 'password2')
     

   
    