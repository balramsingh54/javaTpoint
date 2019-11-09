from django.shortcuts import render
from datetime import datetime
import datetime
# Create your views here.


def home(request):
    mytime = datetime.datetime.now().date()
    mtime = datetime.datetime.now()

    dayofweek =  ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']
    return render(request, 'home.html',{'mytime':mytime, 'dayofweek':dayofweek, 'mtime': mtime})