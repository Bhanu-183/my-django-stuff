from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from firstapp.models import Topic,Webpage,AccessRecord,User

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict={'records':webpage_list,'testing':'hello world'}
    return render(request,'firstapp/index.html',context=date_dict)

def users(request):
    user_list = User.objects.order_by('fname')
    user_dict = {'users': user_list}
    return render(request, 'firstapp/users.html', context=user_dict)
    
def signup(request):
    form = forms.NewUser()
    if request.method == 'POST':
        form = forms.NewUser(request.POST)
        if form.is_valid():
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
    
    