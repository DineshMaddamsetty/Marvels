from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dinesh(request):
    return HttpResponse('<h1><marquee>Hi this is dinesh, Can I have ur Number</marquee></h1>')