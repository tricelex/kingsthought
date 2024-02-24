from django.shortcuts import render, redirect
from lynx.forms import CreateUserForm
from lynx.models import Profile

# Create your views here.
def index(request):
    return render(request, 'lynx/index.html')


def dashboard(request):
    return render(request, 'lynx/dashboard.html')


def register(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            current_user = form.save(commit=False)
            form.save()
            Profile.objects.create(user=current_user)
        return redirect('dashboard')
    else:
        context = {'form': form}
        return render(request, 'lynx/register.html', context)


def login(request):
    return render(request, 'lynx/my-login.html')


def profile(request):
    return render(request, 'lynx/profile-management.html')
