from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def setsession(request):
    request.session['sname']= 'Balram Kumar Singh'
    request.session['semail']= 'singhbalram54@gmail.com'
    return HttpResponse('session is set')

def getsession(request):
    name = request.session['sname']
    email = request.session['semail']
    return HttpResponse(name +" and   "+ email)