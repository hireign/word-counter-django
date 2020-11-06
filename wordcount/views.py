from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def settings(request):
    return HttpResponse('This is settings page')
