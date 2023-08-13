from django.shortcuts import render, redirect
from user_auth_app.forms import UserInfo,UserProfileInfo
from user_auth_app.models import UserProfile

from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):
    registered = False

    if request.method == "POST":
        user = UserInfo(data=request.POST)
        user_profile = UserProfileInfo(data=request.POST)

        if user.is_valid() and user_profile.is_valid():
            user_data = user.save()
            user_data.set_password(user_data.password)
            user_data.save()

            user_profile_data = user_profile.save(commit=False)
            user_profile_data.user = user_data

            if 'picture' in request.FILES:
                user_profile_data.picture = request.FILES['picture']

            user_profile_data.save()

            registered = True

    else:
        user = UserInfo()
        user_profile = UserProfileInfo()
    return render(request, 'form.html', {'forms': user, 'form_profile': user_profile, 'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('user_auth_app:login'))


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return redirect(reverse('base'))
            else:
                return HttpResponse("Account is not active")
        else:
            return HttpResponse("Invalid details supplied ")

    else:
        return render(request, 'login.html')


def base(request):
    return render(request, 'base.html')
