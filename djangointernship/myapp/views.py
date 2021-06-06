from django.shortcuts import render
from django.http import HttpResponse

def  homepageview(request):
    return HttpResponse("<h1>Welcome to Django</h1>")

def  aboutpageview(request):
    return HttpResponse("<h1>About us page</h1>")

def  contactpageview(request):
    return HttpResponse("<h1>Contact us page</h1>")


