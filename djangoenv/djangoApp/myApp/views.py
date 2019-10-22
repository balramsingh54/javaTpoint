from django.shortcuts import render
from myApp.form import stuForm
# Create your views here.

'''
def home(request):
    return render(request, 'home.html')
'''

def home(request):
    stu = stuForm()
    return render(request, 'home.html', {'form':stu})