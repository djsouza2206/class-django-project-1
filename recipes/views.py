from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('My Index!')

def about(request):
    return HttpResponse('Page About!')

def contact(request):
    return HttpResponse('Page Contact!')
