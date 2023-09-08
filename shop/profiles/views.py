from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from profiles.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserPasswordChangeForm
from django.contrib import auth, messages


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'profiles/auth.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('profiles:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'profiles/register.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user)
        password_form = UserPasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid() and password_form.is_valid():
            form.save()
            password_form.save()
            messages.success(request, 'Данные успешно изменены. ')
            return HttpResponseRedirect(reverse('profiles:profile'))
    else:
        form = UserProfileForm(instance=request.user)
        password_form = UserPasswordChangeForm(user=request.user)

    context = {
        'form': form,
        'password_form': password_form,
    }
    return render(request, 'profiles/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))
