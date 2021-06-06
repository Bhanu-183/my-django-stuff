from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from firstapp.models import Topic,Webpage,AccessRecord,User

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict={'records':webpage_list}
    return render(request,'index.html',context=date_dict)

def users(request):
    user_list = User.objects.order_by('fname')
    user_dict = {'users': user_list}
    return render(request, 'users.html', context=user_dict)
    
def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print("Name:", name)
            print("Email", form.cleaned_data['email'])
            print("Text:",form.cleaned_data['text'])
    return render(request, 'form_page.html', context={'form': form})
    