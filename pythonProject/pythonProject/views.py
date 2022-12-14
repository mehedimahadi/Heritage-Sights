# import signin as signin
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib.auth import update_session_auth_hash
from .forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.urls import path, include, re_path
from django.urls import re_path as sign_in
# from django.contrib.auth import signin
from django.contrib.auth.models import User


def heritage(request):
    return render(request, 'heritage.html')


def list_of_sights(request):
    return render(request, 'list_of_sights.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def make_plan(request):
    return render(request, 'make_plan.html')


def home(request):
    return render(request, 'home.html')


def ahsan_manjil(request):
    return render(request, 'ahsan_manjil.html')


def lalbagh_fort(request):
    return render(request, 'lalbagh_fort.html')


def star_mosque(request):
    return render(request, 'star_mosque.html')


def ramakrishna_mission_temple(request):
    return render(request, 'ramakrishna_mission_temple.html')


def profile_page(request):
    return render(request, 'profile_page.html')


def sign_in(request):
    return render(request, 'sign_in.html')


def sign_up(request):
    return render(request, 'sign_up.html')


def reset_with_mail(request):
    return render(request, 'reset_with_mail.html')

def new_pass(request):
    return render(request, 'new_pass.html')


def handleSignup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        if len(name) > 50:
            messages.error(request, "Name must be under 50 characters.")
            return redirect('/sign_up/')
        if password != confirmPassword:
            messages.error(request, "Password don't match try again.")
            return redirect('/sign_up/')

        my_user = User.objects.create_user(name, email, password)
        my_user.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('/')
    else:
        return HttpResponse('404 Not Found')


def handleSignin(request):
    if request.method == 'POST':
        u = request.POST['userName']
        p = request.POST['password']

        user = authenticate(request, username=u, password=p)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In.")
            return redirect('/')
        else:
            messages.error(request, "Something not matching.")
            return redirect('/sign_in/')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')
    return HttpResponse('handleLogout')


def handleContact_us(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        user_email = request.POST['user_email']
        user_message = request.POST['user_message']

        if len(fname) > 50:
            messages.error(request, "Name must be under 50 characters.")
            return redirect('/contact/')

        myuser = models.Contact(UserName=fname, Email=user_email, Message=user_message)
        myuser.save()
        messages.success(request, "Message successfully sent.")
        # return HttpResponse(request, "Your account has been successfully created")
        return redirect('/contact/')
    else:
        return HttpResponse('404 Not Found')


# class PasswordChangeView(PasswordChangeView):
#     form_class = 'new_pass.html'
#     success_url = reverse_lazy(PasswordChangingForm)

def password_success(request):
    return render(request, "home.html")

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        return HttpResponse('404 Not Found')

def password_change_done(request):
    return redirect('/')

def handleProfile(request):
    if request.method == 'POST':
        # username = user.username
        full_name = request.POST['full_name']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']

        if len(full_name) > 50:
            messages.error(request, "Name must be under 50 characters.")
            return redirect('/profile_page/')

        my_user = models.Contact(full_name=full_name, birth_date=date_of_birth,GENRE_CHOICES=gender)
        my_user.save()
        messages.success(request, "Message successfully sent.")
        # return HttpResponse(request, "Your account has been successfully created")
        return redirect('/profile_page/')
    else:
        return HttpResponse('404 Not Found')
