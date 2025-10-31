from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CustomLoginForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        if not user.is_active:
            messages.warning(request, "Your account is pending approval")
            return redirect('login')
        login(request, user)
        messages.success(request, "You are logged in")
        return redirect('home')
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    messages.info(request, "You are logged out")
    return redirect('login')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        messages.success(request, "Registration complete. Await admin approval!")
        return redirect('login')
    return render(request, 'register.html', {'form':form})