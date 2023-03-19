from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.shortcuts import render

from accounts.forms import UserUpdateForm


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


class CustomLogoutView(LogoutView):  # Add this class
    next_page = 'home'



@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=user)

    context = {
        'user': user,
        'form': form
    }
    return render(request, 'accounts/profile.html', context)


