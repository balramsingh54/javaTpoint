from django.shortcuts import render
from datetime import datetime
# Create your views here.


def home(request):
    mytime = datetime.now()
 #   context={'time':mytime}
    return render(request, 'home.html',{'mytime':mytime})
    #return render(request, 'home.html',context)