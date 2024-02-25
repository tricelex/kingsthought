from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, User
from django.shortcuts import render, redirect

from lynx.forms import CreateUserForm, LoginForm, UpdateUserForm, UpdateProfileForm
from lynx.models import Profile


# Create your views here.
def index(request):
    return render(request, 'lynx/index.html')


@login_required(login_url='login')
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'lynx/dashboard.html', context)


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
                auth.login(request, user)
                return redirect('dashboard')

    context = {'form': form}
    return render(request, 'lynx/my-login.html', context)


@login_required(login_url='login')
def profile(request):
    form = UpdateUserForm(instance=request.user)

    profile = Profile.objects.get(user=request.user)
    profile_form = UpdateProfileForm(instance=profile)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'lynx/profile-management.html', context)


def logout(request):
    auth.logout(request)
    return redirect('index')


@login_required(login_url='login')
def delete_account(request):
    if request.method == 'POST':
        delete_user = request.user
        delete_user.delete()
        return redirect('index')
    return render(request, 'lynx/delete-account.html')
