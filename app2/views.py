from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Madhu(request):
    return HttpResponse('<marquee><h1><i>something</i></h1></marquee>')

def nani(request):
    return HttpResponse('<marquee><h1><i>something somthing 😎🙌😍</i></h1></marquee>')