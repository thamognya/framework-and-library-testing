from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def wildcard(request, wildcardurl):
    if (wildcardurl == "blog"):
        return HttpResponse(f'I will figure out how to get multiple html files in react build output to do this render thin')
    else:
        return HttpResponse(f'404 Error: Url {wildcardurl} Not found.')