import random
from django.shortcuts import render


# function based view
def home(request):
    num = random.randint(0, 1000000)
    return render(request, 'base.html', {
        'html_var': True,
        'num': num
    })
