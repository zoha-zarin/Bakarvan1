from django.shortcuts import render , redirect
from .forms import UserRegistrationForm , UserloginForm
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate , login , logout


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user=User.objects.create_user(cd['username'],cd['mobile_phone'],cd['password'])  
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.gender = cd['gender']
            user.save()
            messages.success(request, 'ثبت نام موفقیت آمیز بود')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,'register.html', {'form' : form})



def user_login(request):
    if request.method=='POST':
     form=UserloginForm(request.POST)
     if form.is_valid():
        cd = form.cleaned_data
        user=authenticate(request,mobile_phone=cd['mobile_phone'], password=cd['password'])
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'شماره موبایل یا رمز عبور اشتباه است', 'danger')
    else:
        form=UserloginForm()
    return render(request, 'login.html', {'form':form})



def user_logout(request):
	logout(request)
	messages.success(request, 'خروج موفقیت آمیز بود')
	return redirect('login')