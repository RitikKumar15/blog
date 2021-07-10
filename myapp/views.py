from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Blog
from .forms import AddBlogForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Home
def user_Home(request):
  pi = Blog.objects.all()
  return render(request, 'home.html', {'users': pi})
  
# dashboard
def user_Dashboard(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      fm = AddBlogForm(request.POST)
      if fm.is_valid():
        fm.save()
        return redirect('/')
    else:
      fm = AddBlogForm()
  else:
    return redirect('/login')
  return render(request, 'dashboard.html', {'form': fm})
  
# Profile
def user_Profile(request):
  blog = Blog.objects.all().filter(author=request.user.username)
  return render(request, 'profile.html', {'blog': blog})
  
#deleteblog
def user_Delete(request, id):
  pi = Blog.objects.get(pk=id)
  pi.delete()
  messages.success(request, 'Your Blog Has been Deleted Successful!')
  return redirect('/')
  
#Login
def user_Login(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':
      fm = AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
        username = fm.cleaned_data.get('username')
        password = fm.cleaned_data.get('password')
        validUser = authenticate(username=username, password=password)
        if validUser is not None:
          login(request, validUser)
          return redirect('/')
    else:
      fm = AuthenticationForm()
  else:
    return redirect('/')
  return render(request, 'login.html', {'form':fm})

# Logout
def user_Logout(request):
  logout (request)
  return redirect('/login')

# Signup
def user_SignUp(request):
  if request.method == 'POST':
    fm = SignUpForm(request.POST)
    if fm.is_valid():
      fm.save()
      fm = SignUpForm()
      return redirect('/login')
  else:
    fm = SignUpForm()
  return render(request, 'signup.html', {'form':fm})

# About
def user_About(request):
  if request.user.is_authenticated:
    return render(request, 'about.html')
  else:
    return redirect('/login')
