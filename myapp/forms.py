from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Blog
from django import forms

class AddBlogForm(forms.ModelForm):
  class Meta:
    model = Blog
    fields = ['id', 'author', 'title', 'desc']
    widgets = {
      'title':forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Enter Blog Title...'}),
      'desc': forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Enter Blog Description...'}),
      'author': forms.TextInput(attrs={"class":"form-control", "placeholder":" Enter Your Registered Username Only"})
    }
    labels = {
      'desc': 'Description'
    }
   
class SignUpForm(UserCreationForm):
  password2 = forms.CharField(label='Confirm password(again)', widget = forms.PasswordInput(attrs={'class':'form-control'}))
  password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    labels = {'email':'Email'}
    widgets = {
      'username':forms.TextInput(attrs={'class':'form-control'}),
      'first_name':forms.TextInput(attrs={'class':'form-control'}),
      'last_name':forms.TextInput(attrs={'class':'form-control'}),
      'email':forms.TextInput(attrs={'class':'form-control'})
    }