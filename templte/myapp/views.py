from django.shortcuts import render
from datetime import datetime
import datetime
# Create your views here.


def home(request):
    mytime = datetime.datetime.now().date()
    return render(request, 'home.html',{'mytime':mytime})