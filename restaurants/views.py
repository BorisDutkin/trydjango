import random
from django.shortcuts import render


# function based view
def home(request):

    num = None

    some_list = [
        random.randint(0, 1000000),
        random.randint(0, 1000000),
        random.randint(0, 1000000)
    ]

    condition_bool_item = True

    if condition_bool_item:
        num = random.randint(0, 1000000)

    return render(request, 'base.html', {
        'num': num,
        'some_list': some_list
    })
