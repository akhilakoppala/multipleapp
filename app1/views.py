from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string1(request):
    return HttpResponse('<h1>this is my first string1</h1>')

def string2(request):
    return HttpResponse('<h1>this is my second string2</h1>')
