from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def setCookies(request):
    response =  HttpResponse('cookies is set')
    response.set_cookie('balramkumarsingiloveu','singhbalram054@gmail.com')
    return response

def getcookies(request):
    checkkk = request.COOKIES['balram']
    return HttpResponse("Balram Kumar Singh 1702710054" + " " + checkkk)