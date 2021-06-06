from django.shortcuts import render
from django.http import HttpResponse

from firstapp.models import Topic,Webpage,AccessRecord,User

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict={'records':webpage_list}
    return render(request,'index.html',context=date_dict)


def users(request):
    user_list = User.objects.order_by('fname')
    user_dict = {'users': user_list}
    return render(request,'users.html',context=user_dict)