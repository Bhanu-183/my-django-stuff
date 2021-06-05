from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello world</h1>")

def testing(request):
    my_dict = {
        'name': 'Bhanu',
        'age': 20,
        'gender':'M'
    }
    return render(request,'index.html',context=my_dict)