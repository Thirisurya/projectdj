from django.shortcuts import render
from django.http import HttpResponse

def wish(request):
    message='hiiii'
    return HttpResponse(message)

# Create your views here.
