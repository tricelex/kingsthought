from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from lynx.forms import CreateUserForm, LoginForm
from lynx.models import Profile

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'lynx/index.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'lynx/dashboard.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            current_user = form.save(commit=False)
            form.save()
            Profile.objects.create(user=current_user)
        return redirect('dashboard')
    else:
        context = {'form': form}
        return render(request, 'lynx/register.html', context)


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                auth.login(request, user )
                return redirect('dashboard')

    context = {'form': form}
    return render(request, 'lynx/my-login.html', context)


@login_required(login_url='login')
def profile(request):
    return render(request, 'lynx/profile-management.html')


def logout(request):
    auth.logout(request)
    return redirect('index')
