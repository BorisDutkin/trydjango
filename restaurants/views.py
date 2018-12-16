from django.http import HttpResponse
from django.shortcuts import render


# function based view
def home(request):
    return HttpResponse('hello')
    #return render(request, 'home.html', {})
