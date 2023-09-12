from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from profiles.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserPasswordChangeForm
from django.contrib import auth, messages
from django.contrib.auth import update_session_auth_hash
from wishlist.models import Wishlist

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('profiles:profile'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'profiles/auth.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            if not Wishlist.objects.filter(user=user).exists():
                Wishlist.objects.create(user=user)
            return HttpResponseRedirect(reverse('profiles:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'profiles/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно изменены. ')
            return HttpResponseRedirect(reverse('profiles:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'profiles/profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        password_form = UserPasswordChangeForm(data=request.POST, user=request.user)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request=request, user=request.user)
            messages.success(request, 'Пароль успешно изменен!')
            return HttpResponseRedirect(reverse('profiles:profile'))
    else:
        password_form = UserPasswordChangeForm(user=request.user)

    context = {
        'password_form': password_form,
    }
    return render(request, 'profiles/password_change.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))
