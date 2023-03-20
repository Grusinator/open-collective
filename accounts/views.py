from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from accounts.forms import CustomUserCreationForm, UserUpdateForm  # Update the import


class CustomLoginView(LoginView):
    template_name = 'login.html'


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Update this line to use the custom form
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()  # Update this line to use the custom form
    return render(request, 'signup.html', {'form': form})


class CustomLogoutView(LogoutView):
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
    return render(request, 'profile.html', context)
