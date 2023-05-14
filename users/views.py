from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import User
from users.forms import RegistrationForm
# Create your views here.

def loginPage(request):
    
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)  
        except:
            messages.error(request, 'User doesnt exist')   
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {}
    return render(request, 'users/login_page.html', context)

def register(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:home')
        else:
            context = {'form' : form}
    return render(request, 'users/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')
