from django.shortcuts import render
from django.http import HttpResponse
# Importing forms.py
from . import forms
from firstapp.forms import UserForm,UserProfileInfoform,NewUser,FormName
from django.contrib.auth.models import User
from firstapp.models import Topic, Webpage, AccessRecord, Users, UserProfileInfor


#For Login
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required



def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict={'records':webpage_list,'testing':'hello world'}
    return render(request,'firstapp/index.html',context=date_dict)

def users(request):
    user_list = Users.objects.order_by('fname')
    user_dict = {'users': user_list}
    return render(request, 'firstapp/users.html', context=user_dict)
    
def signup(request):
    form = forms.NewUser()
    if request.method == 'POST':
        form = forms.NewUser(request.POST)
        if form.is_valid():
            # Use form.save to store the input values to the form 
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR")
    return render(request, 'firstapp/user2.html', context={'form': form})
    
def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print("Name:", name)
            print("Email", form.cleaned_data['email'])
            print("Text:", form.cleaned_data['text'])
        else:
            print("Error")
    return render(request, 'firstapp/form_page.html', context={'form': form})
    
    
def register(request):
    registerd = False
    print(registerd)
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoform(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            print("Called")
            user = user_form.save()
            # Use ser_password for hashing
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            # profile user must be linked to the built in User as they are one to one related
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registerd = True
            print(registerd)
        else:
            print('error')
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoform()
        
    return render(request, 'firstapp/register.html', context={'user_form': user_form, 'profile_form': profile_form, 'registerd': registerd})
    


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print("Username {} and password {}".format(username, password))
                return HttpResponse("Account not active")
        else:
            print("Login Failed")
            return HttpResponseRedirect(reverse('register'))
    else:
        return render(request,'firstapp/login.html')
        
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
