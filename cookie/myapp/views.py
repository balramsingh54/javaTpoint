from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def setCookies(request):
    response =  HttpResponse('cookies is set')
    response.set_cookie('balram','balram')
    return response