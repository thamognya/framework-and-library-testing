from django.shortcuts import render
from django.http import Http404, HttpResponse
# Create your views here.
# request -> response
# request handler
# action

def index(request):
    # return HttpResponse(f'Hello')
    return render(request, 'playground/index.html')

def wildcard(request, word_to_say):
    # pull data from db
    # Transofrm 
    # send email
    if (word_to_say == "blog"):
        # return HttpResponse(f'Blog')
        return render(request, 'playground/blog.html')
    elif (word_to_say == "test"):
        # return HttpResponse(f'Test')
        return render(request, 'playground/test.html')
    else:
        #return HttpResponse(f'404 error: /{word_to_say} is not found')
        return render(request, 'playground/error.html', {"context":word_to_say})